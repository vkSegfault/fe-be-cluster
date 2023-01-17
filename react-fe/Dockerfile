FROM node:18.12.1-bullseye AS builder
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build

FROM nginx:1.23.3
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80