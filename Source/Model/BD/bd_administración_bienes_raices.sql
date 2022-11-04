CREATE DATABASE IF NOT EXISTS db_admin_bienes_raices;
USE db_admin_bienes_raices;

/* Tabla Cliente */

CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Cliente 
(
  ID_cliente INT NOT NULL UNIQUE,
  E_mail VARCHAR(25) NOT NULL,
  Tipo_cliente VARCHAR(10) NOT NULL,
  Fecha_alta DATE,
  NyA VARCHAR(45),
  DNI INT NOT NULL UNIQUE,
  Telefono INT NOT NULL,
  Domicilio VARCHAR(50) NOT NULL,
  PRIMARY KEY (ID_cliente)
  );
  
/* Tabla Admin */
  
  CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Admin_Inmobiliario 
(
  Alias_admin  VARCHAR(20) NOT NULL UNIQUE,
  CBU INT NOT NULL UNIQUE,
  NyA VARCHAR(45),
  E_mail VARCHAR(25) NOT NULL,
  Telefono INT NOT NULL,
  Domicilio VARCHAR(50) NOT NULL,
  PRIMARY KEY (Alias_admin)
  );

/* Tabla Clientes_admin */

CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Clientes_admin 
(
  ID_cliente INT NOT NULL,
  Alias_admin VARCHAR(20) NOT NULL,
  Tipo_cliente VARCHAR(10) NOT NULL,
  Fecha_alta DATE,
  E_mail VARCHAR(25) NOT NULL,
  Telefono INT NOT NULL,
  PRIMARY KEY (ID_cliente)
  );

ALTER TABLE db_admin_bienes_raices.Clientes_admin
	ADD FOREIGN KEY (Alias_admin) REFERENCES Admin_Inmobiliario(Alias_admin);

/* Tabla Mensajes */

CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Mensajes
(
  Nro_mensaje INT NOT NULL UNIQUE,
  Asunto VARCHAR(30) NOT NULL,
  Fecha DATE,
  Fecha_alta DATE,
  Descripción_mensaje VARCHAR(70),
  PRIMARY KEY (Nro_mensaje)
  );


/* Tabla Mensajes_Clientes */

CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Mensajes_Clientes
(
  Nro_mensaje INT NOT NULL UNIQUE,
  Alias_admin VARCHAR(20) NOT NULL,
  ID_cliente INT NOT NULL,
  Estado VARCHAR (15) NOT NULL,
  Asunto VARCHAR(30) NOT NULL,
  Fecha DATE,
  Descripción_mensaje VARCHAR(70),
  PRIMARY KEY (Nro_mensaje)
  );
  
ALTER TABLE db_admin_bienes_raices.Mensajes_Clientes
	ADD FOREIGN KEY (ID_cliente) REFERENCES Cliente(ID_cliente),
	ADD FOREIGN KEY (Alias_admin) REFERENCES Admin_Inmobiliario(Alias_admin);
  
/* Tabla Propiedades */

CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Propiedades
(
  ID_propiedad INT NOT NULL UNIQUE,
  Alias_admin VARCHAR(20) NOT NULL,
  Tipo_propiedad VARCHAR(15) NOT NULL,
  Ubicación VARCHAR(50) NOT NULL,
  superficie_m2 INT NOT NULL,
  Cant_ambientes INT NOT NULL,
  Limite_ocupantes INT NOT NULL,
  Permite_mascotas BOOL, 
  Apto_Crédito BOOL,
  Tasación NUMERIC NOT NULL,
  Precio_alquiler NUMERIC NOT NULL,
  PRIMARY KEY (ID_propiedad)
  );
  
ALTER TABLE db_admin_bienes_raices.Propiedades
	ADD FOREIGN KEY (Alias_admin) REFERENCES Admin_Inmobiliario(Alias_admin);
    
/* Tabla Operación */

CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Operación
(
  Nro_operación INT NOT NULL UNIQUE,
  ID_propiedad INT NOT NULL,
  Tipo_operación VARCHAR(15) NOT NULL,
  Fecha_inicio DATE,
  Fecha_fin DATE,
  Comisión NUMERIC,
  Motivo_pago VARCHAR(30) NOT NULL,
  Total_expensas NUMERIC NOT NULL,
  Pago_total NUMERIC NOT NULL,
  PRIMARY KEY (Nro_operación)
  );
  
ALTER TABLE db_admin_bienes_raices.Propiedades
	ADD FOREIGN KEY (ID_propiedad) REFERENCES Propiedades(ID_propiedad);

/* Tabla Comprobante_Pago */

CREATE TABLE IF NOT EXISTS db_admin_bienes_raices.Comprobante_Pago
(
  Nro_comprobante INT NOT NULL,
  Nro_operación INT NOT NULL,
  ID_cliente INT NOT NULL,
  Tipo_comprobante VARCHAR(15) NOT NULL,
  Descripción_operación VARCHAR(70),
  Monto_pagado NUMERIC NOT NULL,
  PRIMARY KEY (Nro_comprobante)
  );
  
ALTER TABLE db_admin_bienes_raices.Comprobante_Pago
	ADD FOREIGN KEY (Nro_operación) REFERENCES Operación(Nro_operación),
    ADD FOREIGN KEY (ID_cliente) REFERENCES cliente(ID_cliente)