function kakaoShare(){
    Kakao.Link.sendDefault({
          objectType: 'feed',
          content: {
            title: '나에게 딱 맞는 노트북',
            description: '세일 가격에 바로 구매하기',
            imageUrl:
              '{{ result_list.0.1}}',
            link: {
              mobileWebUrl: 'https://developers.kakao.com',
              androidExecutionParams: 'test',
            },
          },
          itemContent: {
            profileText: 'Laptop 4 U',
            profileImageUrl: 'https://foru-ffsjy.run.goorm.io/static/main/images/start_page.png',
            titleImageUrl: 'https://foru-ffsjy.run.goorm.io/static/main/images/kakaosharemain.png',
            titleImageText: '노트북 골라드릴게요',
            titleImageCategory: '랩탑 포유',
            items: [
              {
                item: '애플 M1맥북 현재 할인가',
                itemOp: '99만 원',
              },
              {
                item: 'LG 그램 할인가',
                itemOp: '96만 원',
              },
              {
                item: 'Asus 게이밍 노트북 할인가',
                itemOp: '78만 원',
              },
              {
                item: '삼성 갤럭시 북 이온 할인가',
                itemOp: '99만 원',
              },
              
            ],
            sum: '연말까지',
            sumOp: '특별 카드할인',
          },
          social: {
            likeCount: 10,
            commentCount: 20,
            sharedCount: 30,
          },
          buttons: [
            {
              title: '추천 랩탑',
              link: {
                mobileWebUrl: 'https://foru-ffsjy.run.goorm.io/results',
              },
            },
            {
              title: '나도 노트북 찾기',
              link: {
                mobileWebUrl: 'https://foru-ffsjy.run.goorm.io',
              },
            },
          ]
        });
}