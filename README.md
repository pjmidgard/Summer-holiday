# Summer-holiday
Summer holiday

I have written two programs called GOD and DECK_Frech in Python, these games of cards.
I have written a program.
PAQ v77 and AES compression; Speed 200 Bytes-2 KB/s+.
Need to change the name of the file to extract it back and do questions need them.
zstd or zst-.bin... a, b 4.15 v. Speed Max 2KB or 7.32-10MB/s c. 0%-99.8134.
Supercomputer 10GB\s
Cryptography
Compression process percents Max 72%-82% c. Supercomputers 2 hours working were. Sometimes 19 Bytes.
https://www.python.org/downloads/release/python-384/


Zst

Compression

From MySQL Shell 8.0.20, for X Protocol connections and classic MySQL protocol connections, whenever you create a session object to manage a connection to a MySQL Server instance, you can specify whether compression is required, preferred, or disabled for that connection. • required requests a compressed connection from the server, and the connection fails if the server does not support compression or cannot agree with MySQL Shell on a compression protocol. • preferred requests a compressed connection from the server, and falls back to an uncompressed connection if if the server does not support compression or cannot agree with MySQL Shell on a compression protocol. This is the default for X Protocol connections. • disabled requests an uncompressed connection, and the connection fails if the server only permits compressed connections. This is the default for classic MySQL protocol connections. From MySQL Shell 8.0.20, you can also choose which compression algorithms are allowed for the connection. By default, MySQL Shell proposes the zlib, LZ4, and zstd algorithms to the server for X Protocol connections, and the zlib and zstd algorithms for classic MySQL protocol connections (which do not support the LZ4 algorithm). You can specify any combination of these algorithms. The order in which you specify the compression algorithms is the order of preference in which MySQL Shell proposes them, but the server might not be influenced by this preference, depending on the protocol and the server configuration. Specifying any compression algorithm or combination of them automatically requests compression for the connection, so you can do that instead of using a separate parameter to specify whether compression is required, preferred, or disabled. With this method of connection compression control, you indicate whether compression is required or preferred by adding the option uncompressed (which allows uncompressed connections) to the list of compression algorithms. If you do include uncompressed, compression is preferred, and if you do not include it, compression is required. You can also pass in uncompressed on its own to specify that compression is disabled. If you specify in a separate parameter that compression is required, preferred, or disabled, this takes precedence over using uncompressed in the list of compression algorithms. You can also specify a numeric compression level for the connection, which applies to any compression algorithm for X Protocol connections, or to the zstd algorithm only on classic MySQL protocol connections. For X Protocol connections, if the specified compression level is not acceptable to the server for the algorithm that is eventually selected, the server chooses an appropriate setting according to the behaviors listed in Connection Compression with X Plugin. For example, if MySQL Shell requests a compression level of 7 for the zlib algorithm, and the server's mysqlx_deflate_max_client_compression_level system variable (which limits the maximum compression level for deflate, or zlib, compression) is set to the default of 5, the server uses the highest permitted compression level of 5. If the MySQL server instance does not support connection compression for the protocol (which is the case before MySQL 8.0.19 for X Protocol connections), or if it supports connection compression but does not support specifying connection algorithms and a compression level, MySQL Shell establishes the connection without specifying the unsupported parameters. To request compression for a connection from MySQL Shell 8.0.20, use one of the following methods: • If you are starting MySQL Shell from the command line and specifying connection parameters using separate command options, use the --compress (-C) option, specifying whether compression is required, preferred, or disabled for the connection. For example: shell> mysqlsh --mysqlx -u user -h localhost -C required

The --compress (-C) option is compatible with earlier releases of MySQL Shell (back to MySQL 8.0.14) and still accepts the boolean settings from those releases. From MySQL Shell 8.0.20, if you specify just --compress (-C) without a parameter, compression is required for the connection. The above example for an X Protocol connection proposes the zlib, LZ4, and zstd algorithms to the server in that order of preference. If you prefer an alternative combination of compression algorithms, you can specify this by using the --compression-algorithms option to specify a string with a comma-separated list of permitted algorithms. For X Protocol connections, you can use zlib, lz4, and zstd in any combination and order of preference. For classic MySQL protocol connections, you can use zlib and zstd in any combination and order of preference. The following example for a classic MySQL protocol connection allows only the zstd algorithm: shell> mysqlsh --mysql -u user -h localhost -C preferred --compression-algorithms=zstd You can also use just --compression-algorithms without the --compress (-C) option to request compression. In this case, add uncompressed to the list of algorithms if you want to allow uncompressed connections, or omit it if you do not want to allow them. This style of connection compression control is compatible with other MySQL clients such as mysql and mysqlbinlog. The following example for a classic MySQL protocol connection has the same effect as the example above where preferred is specified as a separate option, that is, to propose compression with the zstd algorithm but fall back to an uncompressed connection: shell> mysqlsh --mysql -u user -h localhost --compression-algorithms=zstd,uncompressed You can configure the compression level using the --compression-level or --zstd- compression-level options, which are validated for classic MySQL protocol connections, but not for X Protocol connections. --compression-level specifies an integer for the compression level for any algorithm for X Protocol connections, or for the zstd algorithm only on classic MySQL protocol connections. --zstd-compression-level specifies an integer from 1 to 22 for the compression level for the zstd algorithm, and is compatible with other MySQL clients such as mysql and mysqlbinlog. For example, these connection parameters for an X Protocol connection specify that compression is required for the global session and must use the LZ4 or zstd algorithm, with a requested compression level of 5: shell> mysqlsh --mysqlx -u user -h localhost -C required --compression-algorithms=lz4,zstd --compression-level=5 • If you are using a URI-like connection string to specify connection parameters, either from the command line, or with MySQL Shell's \connect command, or with the shell.connect(), shell.openSession(), mysqlx.getSession(), mysql.getSession(), or mysql.getClassicSession() function, use the compression parameter in the query string to specify whether compression is required, preferred, or disabled. For example: mysql-js> \connect user@example.com?compression=preferred shell> mysqlsh mysqlx://user@localhost:33060?compression=disabled Select compression algorithms using the compression-algorithms parameter, and a compression level using the compression-level parameter, as for the command line options. (There is no zstd-specific compression level parameter for a URI-like connection string.) You can also use the compression-algorithms parameter without the compression parameter, including or omitting the uncompressed option to allow or disallow uncompressed connections. For example, both these sets of connection parameters specify that compression is preferred but uncompressed connections are allowed, the zlib and zstd algorithms are acceptable, and a compression level of 4 should be used: mysql-js> \connect user@example.com:33060?compression=preferred&compression-algorithms=zlib,zstd&compression-level=4 mysql-js> \connect user@example.com:33060?compression-algorithms=zlib,zstd,uncompressed&compression-level=4 • If you are using key-value pairs to specify connection parameters, either with MySQL Shell's \connect command or with the shell.connect(), shell.openSessio

mysqlx.getSession(), mysql.getSession(), or mysql.getClassicSession() function, use the compression parameter in the dictionary of options to specify whether compression is required, preferred, or disabled. For example: mysql-js> var s1=mysqlx.getSession({host: 'localhost', user: 'root', password: 'password', compression: 'required'}); Select compression algorithms using the compression-algorithms parameter, and a compression level using the compression-level parameter, as for the command line and URI- like connection string methods. (There is no zstd-specific compression level parameter for key-value pairs.) You can also use the compression-algorithms parameter without the compression parameter, including or omitting the uncompressed option to allow or disallow uncompressed connections and zeroes and ones.

Who from putting now as this file get say wow but not me.
