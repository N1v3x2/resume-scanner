# Build stage
FROM node:20.18.0-slim AS builder

# Inject the environment variable for React build
ARG VITE_BACKEND_URI
ENV VITE_BACKEND_URI=${VITE_BACKEND_URI}

WORKDIR /app

RUN npm install -g pnpm

COPY package.json pnpm-lock.yaml ./

RUN pnpm install --frozen-lockfile

COPY . .

RUN pnpm run build

# Production stage
FROM nginx

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80