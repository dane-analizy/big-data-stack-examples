# Big Data Stack - przykłady

Przykłady do stacku narzędzi big data zbudowanego w ramach repo [https://github.com/dane-analizy/big-data-stack](big-data-stack).

## Dostępne usługi

- Hadoop UI:      → <http://localhost:9870>
- YARN UI:        → <http://localhost:8088>
- Spark Master UI → <http://localhost:8080>
- Spark Worker UI → <http://localhost:8081>
- Kafka broker:   → localhost:29092 (zewnętrzny listener)
- Mongo UI:       → <http://localhost:8082> (admin / pass)
- NiFi UI:        → <https://localhost:8443>> (login admin / hasło w logach kontenera)

## Kafka

- lista topików:

```bash
docker exec -it broker bash
cd /opt/kafka/bin
./kafka-topics.sh --bootstrap-server broker:9092 --list
```

- utworzenie topika

```bash
docker exec -it broker bash
cd /opt/kafka/bin
./kafka-topics.sh --bootstrap-server broker:9092 --create --topic nazwa_topica
```

- pisanie na topik z konsoli:

```bash
docker exec -it broker bash
cd /opt/kafka/bin
./kafka-console-producer.sh --bootstrap-server broker:9092 --topic nazwa_topica
```

- czytanie z topika w konsoli:

```bash
docker exec -it broker bash
cd /opt/kafka/bin
./kafka-console-consumer.sh --bootstrap-server broker:9092 --topic nazwa_topica
```

## Hadoop

### Podstawowe operacje na HDFS

1. **Wylistowanie plików na HDFS**  
   Wyświetl pliki w katalogu `/input/json/`:

   ```bash
   docker exec -it namenode hdfs dfs -ls /input/json/
   ```

2. **Założenie katalogu na HDFS**  
   Utwórz katalog `/input/json/`:

   ```bash
   docker exec -it namenode hdfs dfs -mkdir -p /input/json/
   ```

3. **Przesłanie plików na HDFS**  
   Wyślij wszystkie pliki JSON z lokalnego katalogu `test-data/pogoda/` do HDFS:

   Jeśli nie masz zmapowanej ścieżki `/local` do hosta w kontenerze, możesz najpierw skopiować pliki do kontenera, a następnie wykonać `hdfs dfs -put`:

   1. Skopiuj pliki z hosta do kontenera (np. do /tmp w kontenerze)

   ```bash
   docker cp ./test-data namenode:/tmp/test-data
   ```

   2. Następnie w kontenerze przenieś pliki do HDFS

   ```bash
   docker exec -it namenode bash
   cd /tmp/test-data
   hdfs dfs -put *.json /input/json/
   ```

   > Alternatywnie możesz zamontować katalog hosta jako wolumen do kontenera przy uruchamianiu dockera.

4. **Pobranie plików z HDFS**  
   Pobierz pliki z katalogu `/input/json/` do lokalnego katalogu:

   ```bash
   docker exec -it namenode hdfs dfs -get /input/json/*.json /local/path/
   ```

> W powyższych przykładach `namenode` to nazwa kontenera z HDFS NameNode.  
> Możesz też użyć `hdfs dfs -...` bezpośrednio, jeśli masz klienta Hadoop na swoim systemie.
