# Flask

`Flask`는 파이썬 기반의  micro framework이다.

## 기본 활용법

1. 설치

   ```bash
   $ pip install flask
   ```

2. 기본 코드

   ```python
   # app.py
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hi():
       return 'Hello!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. 서버 실행

   ```bash
   $ flask run
   ```

   * 기본적으로 `flask run` 명령어는 `app.py`파일을 실행시킨다.

     만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.

   * 마지막 두 줄을 작성해 놓았다면, 아래와 같이 실행도 가능하다.

```bash
$ python app.py
```

## Variable routing

요청 오는 url 변수화 하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'{name}아 안녕?'
```



## Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```
app.py
templates/
	hi.html
	lunch.html
	index.html
```

```python
from flask import Flask, render_template
# ...
@app.route('/hi')
def hi():
    return render_template('hi.html')
```

`HTML` 파일에서 변수의 값을 출력 하고자 한다면, 키워드 인자로 그 값을 넘겨 줘야 한다.

```python
return render_template('hi.html', name=name)
```

그리고 출력을 위해서는 `{{ }}` 사용한다.

``` jinja2
<h1>{{name}} 안녕?</h1>
```

