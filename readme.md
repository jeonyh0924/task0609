
- Model serializer
 
> ModelSerializer 
> > depth = 1



# 햇갈리는 개념 
authentication > 인증이 된건지 아닌건지

authenlization ( permission) >> 인증이 된 유저가 가진 권한이 접근 가능한 권한인지

session -->> 해킹의 위험이 있음

coockie -->> 해킹의 위험이 있음

APi를 사용하는 서버라면 토큰 인증방식을 선택한다. 



#### 1:1 로 매핑을 해야 하기 때문에 저장을 하기 위한 공간이 필요하여 authtoken이란 앱을 사용하면 토큰을 저장하는 테이블을 만들어 두었기 떄문에 installed app에 들어가게 된다. 


### 필터는 글로벌로 설정하지 말고 해당하는 클래스에 적용.