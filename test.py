import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 서비스 계정 키 파일 경로
cred = credentials.Certificate('secrets.json')

# Firebase 앱 초기화
firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()

# 데이터 입력
doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
})

# 데이터 출력
doc_ref = db.collection('users').document('alovelace')
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print('No such document!')


