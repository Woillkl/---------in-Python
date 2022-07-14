''' 
Make Login and Register Program.

Login과 Register 모두 비밀번호 없이 이메일로만 실행한다.

조건 1.
프로그램이 시작되면 유저들에게 2가지의 옵션을 준다.
1. Login     2. Register

조건 2.
1번을 누르면 Login을 하고 2 번을 누르면 회원가입을 한다.

조건 3.
Register를 하게 되면 그 이메일은 user_info.txt 파일에 저장이 된다.

조건 4.
email을 사용자에게 Input 받으면 Input 받은 이메일과 user_info.txt 파일에 있는 이메일들을 비교하여 이메일 유무를 확인한다.
존재할 시, 로그인 성공 메시지 후 프로그램 종료
존재하지 않을 시, 로그인 실패 메시지 후 조건 1번으로 이동

조건 5.
회원가입시 user_info에 중복된 값이 있을 시, 중복 이메일 존재하다고 알린 후 조건 1번으로 이동.
'''