if [ -s text.txt ] && [ -s hello.txt ]
then
        echo "Тесты пройдены"
        echo "Отправляю результаты..."
        send_result_response=$(curl -d "branch=$CI_COMMIT_REF_NAME&nickname=$GITLAB_USER_LOGIN&passed_tests_count=1&total_tests_count=1" \
             -H "Content-Type: application/x-www-form-urlencoded" -H "x-api-key: $TEST_RESULTS_API_KEY" -X POST "$TEST_PASS_URL" \
             --silent --write-out '%{http_code}')
        send_result_status_code=$(echo $send_result_response | tail -c 4)

        if [ "$send_result_status_code" == 200 ];
        then
            echo "Задание выполнено!"
        else
            echo "Ошибка сети. Повтори попытку."
            exit 1
        fi
else
        echo "Тесты провалены"
        exit 1
fi
