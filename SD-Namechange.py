import os

#


#파일이 있는 폴더의 주소를 입력
old_folder_path = r'C:\Users\a01demort\Desktop\7a'

#새롭게 이름이 변경된 다음 옮겨질 폴더주소를 입력
new_folder_path = r'C:\Users\a01demort\Desktop\8b'

if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# png, gif, jpg 확장자 명의 파일만 가능합니다.
# -를 기점으로 왼쪽 내용을 모두 지운 다음 파일을 폴더로 옮겨줍니다.
for filename in os.listdir(old_folder_path):
    if filename.endswith(".png") or filename.endswith(".gif") or filename.endswith(".jpg") :
        new_filename = filename.split("-")[1]
        os.rename(os.path.join(old_folder_path, filename), os.path.join(new_folder_path, new_filename))