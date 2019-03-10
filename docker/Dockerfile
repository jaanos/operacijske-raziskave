# Dockerfile for binder
# Reference: https://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile

FROM sagemath/sagemath:8.6

COPY --chown=sage:sage install.R ${HOME}

USER root

RUN apt-get update && apt-get install --yes --no-install-recommends ca-certificates git libssl-dev make

USER sage

RUN sage -R CMD Rscript ${HOME}/install.R && rm ${HOME}/install.R
