#!/usr/bin/env bash

BASEDIR=$(pwd)
VIDEODIR="${BASEDIR}/videos"
IMAGEDIR="${BASEDIR}/images"
DATADIR="${BASEDIR}/data"

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

for v in $(ls $VIDEODIR/*); do
    FILENAME=$(echo "${v}" | sed "s|${VIDEODIR}/||g");
    BASE64_FILENAME=$(echo "${FILENAME}" | base64 -w 0);
    echo "FILENAME: ${FILENAME}, BASE64_FILENAME: ${BASE64_FILENAME}";

    if [[ ! -d ${IMAGEDIR}/${BASE64_FILENAME} ]]; then

        mkdir -p ${IMAGEDIR}/${BASE64_FILENAME};

        ffmpeg -i ${v} -vf fps=1/15 ${IMAGEDIR}/${BASE64_FILENAME}/%d.png;

        if [[ "$(ls -1 ${IMAGEDIR}/${BASE64_FILENAME}/*png | wc -l)" -gt "0" ]]; then
            echo "${FILENAME}|${BASE64_FILENAME}" >> $DATADIR/video_success_log.txt;
        else
            echo "${FILENAME}|${BASE64_FILENAME}" >> $DATADIR/video_error_log.txt;
        fi;
    fi;
done

IFS=$SAVEIFS