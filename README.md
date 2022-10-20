# s3-file2folder

S3 적재된 파일을 각 파일 이름을 가진 폴더를 생성하고 파일을 복사하는 Trigger Function

## 사용 용도
1. 다수의 .CSV 파일을 Athena에 개별 Table로 적재하기 위한 용도
1. Glue에서는 같은 경로의 .CSV 파일들을 하나의 Table로 인식하므로 .csv 파일들을 개별 폴더로 나누어 복제하고 Glue Crawler를 기동하여 Table 변환을 용이하게 함

## 설치 방법

1. AWS > Lambda > Function 생성 > 코드 복사 후 붙여 넣기 > 배포(Deploy)
1. Lambda > 설정 > 퍼미션 > S3 필요 권한 Policy 생성 후 적용
1. 타겟 버킷 생성(복사할 곳)
1. 타겟 버킷 속성 > 트리거 이벤트 생성 > Object 생성 시 모든 이벤트 적용 후 생성한 Lambda 선택
1. cloud shell 접속 후 파일 복제 

```
//소스 버킷의 `*.csv` 파일들을 타겟 버킷의 `*.csv/*.csv` 로 이동
$ aws s3 cp s3://[소스 버킷]/ s3://[타켓 버킷]/ --exclude "*" --include "*.csv" --recursive

```
