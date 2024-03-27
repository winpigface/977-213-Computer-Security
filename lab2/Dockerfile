FROM --platform=linux/amd64 ubuntu:20.04

RUN apt-get update && \
    apt-get install -y xinetd python3 python3-pip vim

RUN useradd -m ctf

WORKDIR /home/ctf

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./deploy /home/ctf/
RUN pip3 install -r requirements.txt
RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

CMD ["/start.sh"]

EXPOSE 1337
