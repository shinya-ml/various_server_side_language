FROM rust:1.66.0-slim-buster as builder

RUN rustup target add x86_64-unknown-linux-musl \
    && USER=root cargo new --bin app
WORKDIR /app

COPY ./Cargo.toml ./Cargo.toml
COPY ./Cargo.lock ./Cargo.lock

RUN cargo build --release \
    && rm src/*.rs

COPY ./src ./src

RUN rm ./target/release/deps/app* \
    && cargo build --target x86_64-unknown-linux-musl --release

FROM scratch

COPY --from=builder /app/target/x86_64-unknown-linux-musl/release/app .

CMD ["./app"]