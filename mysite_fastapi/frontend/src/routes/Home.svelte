<script>
    // 빈 리스트로 초깃값을 주지 않으면 fetch 함수는 비동기 방식으로 실행되어,
    // 요청하는 중에 each문이 실행되고 question_list에 값이 없어 오류가 발생한다.
    let question_list = []
  
    // get_quesiton_list()는 질문 목록 API를 호출하는 함수다. 
    // 호출하여 얻은 quesiton_list는 each문을 순회하며 제목을 표시한다.
    function get_question_list() {
      fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
        response.json().then((json) => {
          question_list = json
        })
      })
    }
  
    get_question_list()
  </script>
  
  <ul>
    {#each question_list as question}
      <li>{question.subject}</li>
    {/each}
  </ul>