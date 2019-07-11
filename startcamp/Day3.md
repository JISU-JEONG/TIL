# Day3

## HTML/CSS

### HTML

`HTML`은 HyperText Markup Language의 약자로 웹문서를 구조화 하는데 사용되는 언어이다.

1. HTML 기본 구조

   ```html
   <!--emmet-->
   <!--! + tap 하면 html 기본 형식이 완성-->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       <!--jinja2 템플릿 언어-->
       <h1>{{name}}아 안녕?</h1>
   </body>
   </html>
   ```

   * `<head> </head>` 는 문서의 정보를 담고 있다.
   * `<body> </body>` 는 문서의 본문을 담고 있다.

2. 태그의 종류

   1. 기본적으로 태그는 `여는태그`와`닫는태그` 로 구성된다.

      ```html
      <h1>제목1</h1>
      ```

   2. `닫는태그`가 없는 경우도 있다.(self-closing tag)

      ```html
      <img src="__"/>
      ```

1. 태그의 구성

      ```html
      <img src="____" width="300" height="300" class="img-blue"/>
      <a href="https://google.com" class="blue">구글</a>
      ```

      * 태그별로 공통적으로 가질 수 있는 속성 : `id`, `class`, `style`
      * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
        * img -`src`, `width`, `height`
        * a - `href`



### CSS

CSS는 Casecading Style Sheets의 약자로, HTML을 꾸며주는 역활을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)`를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   * 태그 선택자

     ```CSS
     P{
         color : red;
     }
     ```

   * class 선택자

     ```CSS
     .blue{
         color: blue;
     }
     ```

   * id 선택자

     ```CSS
     #pink{
     	color: pink;
     }
     ```

   선택자 우선순위는 id 선택자 > class 선택자 > 태그 선택자 순서로 적용된다.



## Flask Template Engine - jinja2

Flask는 기본적으로 Template을 만들 때 `jinja2` 를 사용한다.



1. 값 출력

   ```jinja2
   <h1> {{ name }}, 안녕? </h1>
   ```

2. 조건문

   ```jinja2
   {% if name == '용흠' %}
   	<h1>반장님 안녕하세요.</h1>
   {% else %}
   	<h1>학생들 ㅎㅇ</h1>
   {% endif %}
   ```

3. 반복문

   ```jinja2
   {% for menu in menu_list%}
   	<li>{{ menu }}</li>
   {% endfor %}
   ```

