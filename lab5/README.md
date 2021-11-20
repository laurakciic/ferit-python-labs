500  git clone https://gitlab.com/kovaciclaura/se_labs.git
  501  git clone https://gitlab.com/kovaciclaura/se_labs.git
  502  git config user.name "laura"
  503  cd se_labs/
  504  git config user.name "laura"
  505  git config user.email "laurakciic@gmail.com"
  506  ls
  507  code .
  508  code .
  509  cd lab5
  510  python -m venv django
  # creating virtual env named django

  511  ls
  512  source django/Scripts/activate
  # activating virutal env

  513  pip install django
  # installing django framework

  514  django-admin --version
  # checking for correct installation

  515  django-admin startproject myimgur
  # creating initial project

  516  ls
  517  cd myimgur/
  518  ls
  519  winpty python manage.py runserver
  # starting server
  # winpty is only for windows

  520  winpty python manage.py runserver
  521  cd ..
  522  cd ..
  523  git status
  524  git status
  525  git add lab5
  526  git status
  527  git commit -m "add myimgur inital project to lab5"
  528  git add .gitignore
  529  git status
  530  git commit --amend
  # merging this commit with previous commit 

  531  git status
  532  history
(django)

 533  git status
  534  git add lab5/README.md
  535  git commit -m "add git commands and their explanations to README.md"
  536  clear
  537  pip freeze
  # ispisuje verzije paketa na ekran

  # udemo u dir gdje zelimo napraviti requirements.txt file 
  538  cd lab5

  # ispis potrebnih paketa u requirements.txt
  539  pip freeze > requirements.txt
  540  ls

  # instalacija potrebnih paketa iz requirements.txt filea
  542  pip install -r requirements.txt
  543  history
(django)

