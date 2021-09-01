import pickle   # 따로 인코딩 필요 없다. 
profile_file = open("profile.pickle", "wb")  # w는 쓰기 용도 b는 바이너리
profile = {"이름": "야통이", "나이" :3, "취미":["그루밍하기", "애교부리기"]}
print(profile)
pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장.
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
