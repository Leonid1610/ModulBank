FROM python:3-stretch

COPY . /ModulBank
WORKDIR /ModulBank

RUN chmod +x allure/bin/allure

RUN pip install -r requirements.txt;

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer;

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN export JAVA_HOME

CMD py.test tests -v -l --alluredir=allure_result; cd allure/bin/; ./allure serve ../../allure_result --host 172.17.0.2 --port 8080