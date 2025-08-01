//sever.js
const express = require('express'); // Express 프레임워크를 불러옵니다. 웹 애플리케이션을 만들고 라우팅을 처리하는 데 사용됩니다.
const path = require('path');     // 파일 및 디렉토리 경로 작업을 위한 Node.js 내장 모듈입니다.
const axios = require('axios');   // HTTP 요청을 보내기 위한 Promise 기반 클라이언트입니다. 외부 API와 통신하는 데 사용됩니다.
const app = express();            // Express 애플리케이션 인스턴스를 생성합니다.
const port = 3000;                // 서버가 수신 대기할 포트 번호를 정의합니다.

// 미들웨어 설정
app.use(express.json()); // 요청 본문(body)에 있는 JSON 데이터를 파싱하여 JavaScript 객체로 만들어줍니다.
// '..\frontend' 경로는 현재 스크립트 파일이 있는 디렉토리(backend)에서 한 단계 상위로 이동한 후 frontend 디렉토리를 가리킵니다.
app.use(express.static(path.resolve(__dirname, '..', 'frontend'))); // 'frontend' 디렉토리의 정적 파일(HTML, CSS, JS 등)을 서비스하도록 설정합니다.

// 루트 경로 ('/')에 대한 GET 요청 처리
app.get('/', (req, res) => {
  // 클라이언트가 웹 애플리케이션의 기본 URL로 접속하면 'index.html' 파일을 전송합니다.
  res.sendFile(path.resolve(__dirname, '..', 'frontend', 'index.html'));
});

// '/check-breach' 경로에 대한 POST 요청 처리 (이메일 유출 확인 API)
app.post('/check-breach', async (req, res) => {
  const { email } = req.body; // 요청 본문에서 'email' 값을 추출합니다.
  const hibpApiKey = 'API_KEY'; // Have I Been Pwned (HIBP) API 키를 설정합니다. 실제 사용 시에는 발급받은 키로 교체해야 합니다.

  try {
    // HIBP API에 GET 요청을 보냅니다.
    const response = await axios.get(`https://haveibeenpwned.com/api/v3/breachedaccount/${email}`,
      {
        headers: {
          'hibp-api-key': hibpApiKey, // HIBP API 인증을 위한 API 키를 헤더에 포함합니다.
          'user-agent': 'pwned-check-app' // API 요청 시 User-Agent 헤더를 설정하여 요청을 식별합니다.
        }
      }
    );
    // HIBP API로부터 받은 응답 데이터를 클라이언트에게 JSON 형태로 반환합니다.
    res.json(response.data);
  } catch (error) {
    // 오류 처리
    if (error.response && error.response.status === 404) {
      // HIBP API에서 404 (Not Found) 응답을 받은 경우, 해당 이메일이 유출되지 않았음을 의미합니다.
      res.json({ message: 'No breaches found for this email.' });
    } else {
      // 그 외의 다른 오류가 발생한 경우 (예: 네트워크 문제, API 키 오류 등)
      console.error('Error checking for breaches:', error); // 서버 콘솔에 오류를 기록합니다.
      res.status(500).json({ error: 'An error occurred while checking for breaches.' }); // 클라이언트에게 500 상태 코드와 오류 메시지를 반환합니다.
    }
  }
});

// 서버 시작
app.listen(port, () => {
  // 서버가 지정된 포트에서 성공적으로 시작되면 콘솔에 메시지를 출력합니다.
  console.log(`Server is running on http://localhost:${port}`);
});
