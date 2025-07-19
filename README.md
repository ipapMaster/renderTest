# Deploy на Render (https://render.com/)
**Render** — это современная облачная платформа, которая позволяет легко развертывать и хостить веб-приложения. 

1. Cтруктура проекта выглядит так:

```
/your-project
├── Procfile
├── web.py
├── requirements.txt
└──...
```

2. В файле Procfile, должно быть:
```web: gunicorn -b 0.0.0.0:$PORT web:app```

3. В requirements.txt указать:

```Flask
gunicorn
gevent```

4. В web.py:

```Python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Render!"

if __name__ == '__main__':
    app.run()
```


Пошаговая инструкция по развертыванию
* Зарегистрируйтесь на Render
* Подключите GitHub/GitLab аккаунт
* Нажмите кнопку New → Web Service
* Выберите репозиторий с вашим проектом
* Нажмите кнопку Deploy
* Дождитесь завершения сборки
