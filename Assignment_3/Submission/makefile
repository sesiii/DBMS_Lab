runcpp:
	g++ db.cpp -o db -lpqxx -lpq
	./db

runpy:
	# python -m venv myenv
	# source myenv/bin/activate
	# pip install psycopg2-binary
	# pip install tabulate
	python3 db.py

compilejava:
	javac -cp postgresql-42.7.5.jar DBManager.java

runjava: compilejava
	java -cp .:postgresql-42.7.5.jar DBManager

clean:
	rm -f db