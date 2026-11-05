FROM golang:1.27-alpine AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY cmd ./cmd
COPY internal ./internal
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /vietlott-crawler ./cmd/vietlott

FROM alpine:3.22
RUN apk add --no-cache ca-certificates tzdata
COPY --from=build /vietlott-crawler /usr/local/bin/vietlott-crawler
# the crawler locates the repo root by finding data/ and crawler/ directories
RUN mkdir -p /repo/crawler /repo/data
WORKDIR /repo
ENV TZ=Asia/Ho_Chi_Minh
ENTRYPOINT ["vietlott-crawler"]
CMD ["status"]
