**Diese Repository wurde im Rahmen einer Semesterarbeit erstellt und dient dazu einen Flink Cluster mit Hilfe von Docker aufzusetzten.**

1. starten des Clusters `docker compose up`
2. stoppen des Clusters `docker compose down`
3. start eines Flinkjobs `./run-job.sh class jar parallelism`
   z.B. `./run-job.sh org.gradoop.tutorial.operators.subgraph.SubgraphTutorial_1 gradoop-tutorial/target/gradoop-tutorial-1.0.jar 24`
   Der parallelism Wert ist optional.
   Für Logging: `./run-job.sh org.gradoop.tutorial.operators.subgraph.SubgraphTutorial_1 gradoop-tutorial/target/gradoop-tutorial-1.0.jar 24 >> log.log`
   Ein Testdatensatz befindet sich im orig Ordner. Dieser stammt aus folgender Repository: https://github.com/dbs-leipzig/gradoop-tutorial
