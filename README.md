# Laptop 4 U

Welcome to Laptop 4 U!

## ~211108 개발일지

### isoomni

    + DONE
    	- foru container 시작 및 환경설정
    	- apps.py 생성
    	- database models.py 로 생성 및 관리
    	- templates 생성 및 models.py, views.py와 index.html 연결
    	- 개발한 프론트 git 공유
    	- project container 구조 설명 업로드
    	- README.md 개발일지 틀 만들고 팀원들에게 이용 권유

    + TODO
    	- ERD 수정
    	- DJango 필터링 구조 공부

## 211109 개발일지

### EUNJEONG

    + Done
        - templates 하위 디렉토리 main 생성
        - templates/main에 index.html 이동, details.html, results.html 생성

## 211110 개발일지

### CHANHYEOK
    
    + Done
        - 메인페이지 구상
        - 이미지 파일 추가
        - css 파일 추가
    
    +TODO
        - css 연결
        - 질문페이지 구상
        - 시작버튼 연결

## 211111 개발일지

### isoomni, EUNJEONG, 0104suyeon

    + DONE
    	- 첫번째 페이지
    	- count 추가
    	- erd 설계 수정
    	- database - model.py(class Laptop, class Question, class Choice)
    	- css 연결

    +TODO
    	- laptop dumy data → 준석 10개
    	- choice, question dummy data→ 4은정/3수민/3수연
    	- erd 수정

    + 전달 사항
    	- 첫 번째 페이지에 Laptop별 count 추가
    	- css 및 스타일 파일은 static에

## 211113 개발일지

### EUNJEONG

    + DONE
    	- admin 페이지 수정
    		- question 페이지에서 choice 편집 가능 하도록 변경
    	- models.py
    		- battery FloatField로 수정
    		- status default 값 수정
    		- card_discount max_length 10으로 수정
    	- main/urls.py 파일 생성
    		- 메인 화면 들어올 때 index.html 보여주도록 url 설정

    + TODO
        - admin페이지에서 question 추가 시 발생하는 오류 파악
            - NOT NULL constraint failed: main_question.created_at

## 211115 개발일지

### isoomni

    + DONE
    	- admin페이지에서 question 추가 시 발생하는 오류 해결
            - NOT NULL constraint failed: main_question.created_at
    		- default가 없는데 null=true가 빠진 부분이 있었음. created_at에도 null=true 해줌.
    	- views.py 에 index, details, results 함수 생성 및 쿼리 작성
    	- views.py details 함수에 question response 하도록 api 작성 (print로 확인할 수 있게 해둠.)
    	- details.html 연결

    + TODO
    	- 2번 질문을 참을성이 있으신가요? 전 참지 않아요 등으로 더 추상적으로 바꾸는게 어떨까요?

## 211116 개발일지

### EUNJEONG

    + DONE
    	- choice, question, Laptop API 페이지 생성
    		- serializers.py
    		- ~/api/choice/
    		- ~/api/question/
    		- ~/api/laptop/
            

## 211119 개발일지

### CHANHYEOK
    
    +DONE
        -MainPage 추가
            -노트북 추천 애니메이션 추가
            -노트북 검사 결과 순위 표시 추가
            
    +TODO
        -QuestionPage 구현
        -ResultPage 점검 및 수정

## 211126 개발일지

### CHANHYEOK
    
    +DONE
        - 질문페이지 구현
        - 질문페이지 CSS연결


## 211128 개발일지

### EUNJEONG, isoomni, 0104suyeon

    +DONE
        - views.py의 def result 수정
            - details.html에서 input 값 가져옴
            - input 값 바탕으로 필터링 구현
        - details.html 질문 출력 방식 수정

## 211130 개발일지

### EUNJEONG

    +DONE
        - Q() 사용하여 filter 추가
        - input 값 필터링 부등호 조건 만족
        
    +TODO
        - question6 용도 구분 필요
        
## 211202 개발일지

### EUNJEONG, isoomni, 0104suyeon

    + DONE
        - 필터링 구현 완료
        - results.html 페이지로 넘기기 완료
        - all_laptops.html 페이지 구현
    
    + TODO
        - 노트북 카운트 구현
        - 유사한 다른 노트북 구현

### CHANHYEOK
    + DONE
        - 질문 페이지 이전, 다음버튼 구현
        - 스크롤js 기능 구현 및 연결
        
    + TODO
        - 질문페이지 CSS수정
        - 질문 사진 추가
        - 전체 노트북 조회 페이지 구현
                
## 211205 개발일지

### EUNJEONG, isoomni, 0104suyeon

    + DONE
        - 유사한 다른 노트북 조회 구현
        - 노트북 카운트 구현
        - 서버 끝!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>.<

## 211206 개발일지

### CHANHYEOK
    
    + DONE
        - 모든 노트북 조회 페이지 카드형식 구현
        - 모든 노트북 조회 페이지 CSS 연결
        - 모든 노트북 조회 페이지 홈버튼 구현

    +TODO
        - 모든 노트북 조회 페이지 반응형
        - 질문 페이지 질문 간격 CSS 수정
        - 질문 페이지 이미지 추가 및 디자인 보완

## 211207 개발일지

### CHANHYEOK

    + DONE
        - 질문 페이지 이미지 추가 및 디자인 보완
        - 질문 페이지 진행정도 표시 추가
        - 결과 및 결과없음 페이지 배경화면, 글꼴 추가

    +TODO
        - 모든 노트북 조회 페이지 반응형
        - 질문 페이지 질문 간격 CSS 수정


## 211208 개발일지

### CHANHYEOK

    +DONE
        - 메인페이지 최종 점검
        - 질문페이지 질문 CSS수정
        - 결과페이지 배경화면 수정
        - 모든 노트북 조회 페이지 반응형 설정
        
    +TODO
        - 결과페이지 반응형 구현
        - 시작페이지 순위 확인
        
        
