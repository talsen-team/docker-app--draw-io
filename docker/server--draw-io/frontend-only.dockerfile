FROM nginx:alpine

ENV BUILD_DRAW_IO_VERSION=v10.1.2

RUN apk update                                         \
 && apk add --no-cache                                 \
            --virtual .install-dependencies            \
            git                                        \
 && rm -rf                                             \
       /usr/share/nginx/html                           \
 && mkdir -p                                           \
          /usr/share/nginx/html                        \
 && git clone https://github.com/jgraph/drawio.git     \
              --recurse-submodules                     \
              --branch ${BUILD_DRAW_IO_VERSION}        \
              /tmp/app-draw-io                         \
 && cp -r                                              \
       /tmp/app-draw-io/src/main/webapp/.              \
       /usr/share/nginx/html                           \
 && rm -rf                                             \
       /tmp/app-draw-io                                \
 && apk del .install-dependencies
 