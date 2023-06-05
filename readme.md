this is an task performed for creating user_registeration_login interface.

follow below steps to setup the application in your environment:

step 1 : clone the repo.

step 2 : at root level create a python virtual env, 
            -> at root run :- python -m venv <name of your virtual environment>.
            -> if you are on linux run :- source <name of your virtual environment>/bin/activate.

            ** the above steps will create and activate the virtual env for your development **

step 3 : now we will install required python libraries,
            -> pip install -r requirements.txt.

            ** this will install all required python libraries **

step 4 : need to set system env vars to use Gmail smtp service,
            ** to use the Gmail SMTP service you need to do some adjustments in your gmail account from which you will send the email, the link to resource 
            for the same : https://www.youtube.com/watch?v=iGPPhzhXBFg **

            -> in linux open terminal and run :- export EMAIL_HOST_USER=<your Gmail Host account address> 
                                              :- export EMAIL_HOST_PASSWORD=<your app password generated by gmail account>

                                              ** above video link will tell you how to generate and use app password for enabling smtp service for your gmail account **
            
** now lets see the steps to start the application **

step 5 : now from the manage.py script level run :- python manage.py makemigrations
                                            then :- python manage.py migrate

step 6 : now start the application :- python manage.py runserver.


** the above steps will run this application , but follow the steps in order **.

** the application will behave in two parts :

    -> first it will ak for your email address, then on clicking the register button you will redirect to otp_verification , if you are already a part of system/application there will be new otp generated for you shared to the given email address else it will make you part of process and share the otp with you.

    