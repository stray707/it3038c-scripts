#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')
VENTCURRENTLY=$(echo $DATA | jq '.[0].onVentilatorCurrently')
ICUCURRENTLY=$(echo $DATA | jq '.[0].inIcuCurrently')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests, $DEATHS deaths (an increase of $DEATHINCREASE from yesterday), $HOSPITALIZED hospitalized, $VENTCURRENTLY people currently on ventilators, and $ICUCURRENTLY people currently in ICU."
