FROM gojo07/gojo-userbot:buster

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b Gojo-Userbot https://github.com/Cloder07/Gojo-Userbot /home/Gojo-Userbot/ \
    && chmod 777 /home/Gojo-Userbot \
    && mkdir /home/Gojo-Userbot/bin/

COPY ./sample_config.env ./config.env* /home/Gojo-Userbot/

WORKDIR /home/Gojo-Userbot/

RUN pip install -r requirements.txt

CMD [ "bash", "start" ]
