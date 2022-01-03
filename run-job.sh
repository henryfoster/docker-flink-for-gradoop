#!/bin/bash
#./job-run.sh dnaow.dnha.wodn ~/myjar.jar

if [ -f .env ]
then
  export $(cat .env)
fi

if [ -z $1 ] ; then
  echo "You need to specify a job class!" && exit 1;
fi

if [ -z $2 ] ; then
  echo "You need to specify the path to the jar!" && exit 2;
fi

jobClass="$1"
filePath="$2"
calculatedParallelism=$(expr $TASKMANGER_NUMBER_OF_TASK_SLOTS \* $SCALE)
parallelism="${3:-$calculatedParallelism}"
containerId=$(docker ps --filter name=jobmanager -q)
echo $TASKMANGER_NUMBER_OF_TASK_SLOTS
sudo cp -r orig/ldbc_sample /tmp/gradoop-input/ldbc_sample

sudo chmod o+w /tmp/gradoop-output
docker cp $filePath $containerId:/job.jar
docker exec -it $containerId flink run -p $parallelism -c $jobClass /job.jar