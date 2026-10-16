#!/bin/zsh
set -eu
BLOG_SITE_ROOT="${0:A:h:h}"
cd "$BLOG_SITE_ROOT"
exec "$BLOG_SITE_ROOT/runtime/hugo" --cacheDir "$BLOG_SITE_ROOT/runtime/cache" --gc --minify "$@"
