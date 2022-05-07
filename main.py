def list_uploading(file_list):
    import requests

    from pprint import pp, pprint

    from yandex import YaUploader

    ya_token ='' #Здесь должен быть ваш token от Яндексдиска

    if __name__ == '__main__':
        yadisk = YaUploader(ya_token)
        for name in file_list:
            file_path = f"/{name}"
            yadisk.upload_file(file_path, {name})

list_uploading(['photo.jpg', 'text_file.txt'])





