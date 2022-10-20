import boto3
import urllib

def lambda_handler(event, context):
    
    # 트리거 이벤트로 전달 받은 버킷과 키 이름
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    # 루트 버킷에 업로드된 오브젝트만 복제 적용(무한 루프 방지)
    if '/' not in key:
        
        # Copy object
        s3_client = boto3.client('s3')
        s3_client.copy_object(
            Bucket = bucket,
            Key = f"{key}/{key}",
            CopySource= {'Bucket': bucket, 'Key': key}
        )
        
        # Delete source object
        s3_client.delete_object(
            Bucket = bucket,
            Key = key
        )
