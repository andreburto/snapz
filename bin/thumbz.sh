#!/usr/bin/env bash

BASEDIR=$(pwd)
IMAGEDIR="${BASEDIR}/images"
THUMBDIR="${BASEDIR}/thumbs"

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

for d in $(ls -d ${IMAGEDIR}/*); do
    BASE64_VIDEONAME=$(echo "${d}" | sed "s|${IMAGEDIR}/||g");

    if [[ ! -d ${THUMBDIR}/${BASE64_VIDEONAME} ]]; then

        mkdir -p ${THUMBDIR}/${BASE64_VIDEONAME}

        for i in $(ls ${IMAGEDIR}/${BASE64_VIDEONAME}/*png); do
            IMAGENAME=$(echo "${i}" | sed "s|${IMAGEDIR}/${BASE64_VIDEONAME}/||g");
            magick $i -resize x100 "${THUMBDIR}/${BASE64_VIDEONAME}/th_${IMAGENAME}"
        done;
    fi
done;

IFS=$SAVEIFS
