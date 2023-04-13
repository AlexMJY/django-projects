// operation: 데이터를 처리하는 방법, 소문자만 사용한다. ex) get, post, put, delete
// url: 요청 URL, 단 백엔드 서버의 호스트명 이후의 URL만 전달 ex) /api/question/list
// params: 요청 데이터 ex) {page: 1, keyword: "markdown"}
// success_callback: API 호출 성공시 수행. json이 입력으로 주어진다.
// failure_callback: API 호출 실패시 수행. 전달된 함수에는 오류 값이 입력으로 주어진다.

const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params)

    // operation이 get인 경우에 GET 방식에 맞게끔 파라미터 url을 조립.
    let _url = import.meta.env.VITE_SERVER_URL+url // .env 파일
    if(method === 'get') {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }

    if (method !== 'get') {
        options['body'] = body
    }

    fetch(_url, options)
        .then(response => {
            response.json()
                .then(json => {
                    if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                        if(success_callback) {
                            success_callback(json)
                        }
                    }else {
                        if (failure_callback) {
                            failure_callback(json)
                        }else {
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi