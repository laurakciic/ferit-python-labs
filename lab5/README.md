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



# novi terminal
501  cd lab5/
  502  source django/Scripts/activate
  503  cd myimgur/
  504  python manage.py migrate
  505  git status
  506  git add db.sqlite3
  507  python manage.py createsuperuser
  508  winpty python manage.py createsuperuser
  509  git status
  510  git add db.sqlite3
  511  git status
  512  git commit -m "apply migrations and create superuser"
  513  python manage.py startapp images
  514  git add *
  515  git status
  516  git commit -m "myimgur inital"
  517  git add *
  518  git status
  519  git commit -m "add html basic implementation"
  520  git push
  521  git add *
  522  git status
  523  git commit -m "add css.style"
  524  git push
  525  git add *
  526  git status
  527  git commit -m "add base template"
  528  git push
  529  python manage.py makemigrations
  530  git status
  531  python manage.py migrate
  532  git status
  533  git diff db.sqlite3
  534  git add *
  535  git commit -m "add Image and Comment models"
  536  git push
  537  git add *
  538  git commit -m "add image urls and comments"
  539  git push
  540  git add *
  541  git commit -m "add detail.html and other"
  542  history

