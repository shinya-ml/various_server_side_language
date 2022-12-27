FROM rust:1.66.0

WORKDIR /app
COPY ./app /app

RUN cargo build --release
RUN cargo install --path .

CMD ["app"]