-- ============================================================
-- CREAR BASE DE DATOS
-- ============================================================

CREATE DATABASE IF NOT EXISTS adso3294089
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE adso3294089;


-- ============================================================
-- 1. ELIMINAR TABLAS EXISTENTES
-- ============================================================

DROP TABLE IF EXISTS t_mat_eva;
DROP TABLE IF EXISTS t_imparte;
DROP TABLE IF EXISTS t_matricula;
DROP TABLE IF EXISTS t_instructor;
DROP TABLE IF EXISTS t_aprendiz;
DROP TABLE IF EXISTS t_evaluacion;
DROP TABLE IF EXISTS t_curso;
DROP TABLE IF EXISTS t_persona;


-- ============================================================
-- 2. TABLA PERSONA
-- ============================================================

CREATE TABLE t_persona (
    PER_ID INT NOT NULL AUTO_INCREMENT,
    PER_UUID VARCHAR(37) NOT NULL,
    PER_PRI_NOMBRE VARCHAR(15) NOT NULL,
    PER_SEG_NOMBRE VARCHAR(15) DEFAULT NULL,
    PER_PRI_APELLIDO VARCHAR(15) NOT NULL,
    PER_SEG_APELLIDO VARCHAR(15) DEFAULT NULL,
    PER_DOC BIGINT NOT NULL,

    PRIMARY KEY (PER_ID),
    UNIQUE KEY UK_PERSONA_UUID (PER_UUID),
    UNIQUE KEY UK_PERSONA_DOC (PER_DOC)

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


-- ============================================================
-- 3. TABLA CURSO
-- ============================================================

CREATE TABLE t_curso (
    CUR_ID INT NOT NULL AUTO_INCREMENT,
    CUR_UUID VARCHAR(37) NOT NULL,
    CUR_NOMBRE VARCHAR(35) NOT NULL,
    CUR_CODIGO INT NOT NULL,
    CUR_DURACION INT NOT NULL,
    CUR_DESCRIPCION VARCHAR(100) NOT NULL,
    CUR_COSTO DECIMAL(12,2) DEFAULT NULL,

    PRIMARY KEY (CUR_ID),
    UNIQUE KEY UK_CURSO_UUID (CUR_UUID),
    UNIQUE KEY UK_CURSO_CODIGO (CUR_CODIGO)

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


-- ============================================================
-- 4. TABLA EVALUACION
-- ============================================================

CREATE TABLE t_evaluacion (
    EVA_ID INT NOT NULL AUTO_INCREMENT,
    EVA_UUID VARCHAR(37) NOT NULL,
    EVA_NOMBRE VARCHAR(45) NOT NULL,
    EVA_CODIGO INT NOT NULL,
    EVA_PORCENTAJE DOUBLE NOT NULL,
    EVA_DATE DATE NOT NULL,

    PRIMARY KEY (EVA_ID),
    UNIQUE KEY UK_EVALUACION_UUID (EVA_UUID),
    UNIQUE KEY UK_EVALUACION_CODIGO (EVA_CODIGO)

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


-- ============================================================
-- 5. TABLA APRENDIZ
-- ============================================================

CREATE TABLE t_aprendiz (
    APR_ID INT NOT NULL AUTO_INCREMENT,
    APR_UUID VARCHAR(37) NOT NULL,
    APR_FECHA_NAC DATE NOT NULL,
    APR_PER_ID INT NOT NULL,

    PRIMARY KEY (APR_ID),

    UNIQUE KEY UK_APRENDIZ_UUID (APR_UUID),
    UNIQUE KEY UK_APRENDIZ_PERSONA (APR_PER_ID),

    CONSTRAINT FK_APRENDIZ_PERSONA
        FOREIGN KEY (APR_PER_ID)
        REFERENCES t_persona (PER_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


-- ============================================================
-- 6. TABLA INSTRUCTOR
-- ============================================================

CREATE TABLE t_instructor (
    INS_ID INT NOT NULL AUTO_INCREMENT,
    INS_UUID VARCHAR(37) NOT NULL,
    INS_ESPECIALIDAD VARCHAR(20) NOT NULL,
    INS_PER_ID INT NOT NULL,

    PRIMARY KEY (INS_ID),

    UNIQUE KEY UK_INSTRUCTOR_UUID (INS_UUID),
    UNIQUE KEY UK_INSTRUCTOR_PERSONA (INS_PER_ID),

    CONSTRAINT FK_INSTRUCTOR_PERSONA
        FOREIGN KEY (INS_PER_ID)
        REFERENCES t_persona (PER_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


-- ============================================================
-- 7. TABLA IMPARTE
-- Relaciona instructores con cursos
-- ============================================================

CREATE TABLE t_imparte (
    IMP_ID INT NOT NULL AUTO_INCREMENT,
    IMP_UUID VARCHAR(37) NOT NULL,
    IMP_ROL VARCHAR(45) NOT NULL,
    IMP_FECHA_ASIGNACION DATE NOT NULL,
    IMP_CUR_ID INT NOT NULL,
    IMP_INS_ID INT NOT NULL,

    PRIMARY KEY (IMP_ID),

    UNIQUE KEY UK_IMPARTE_UUID (IMP_UUID),

    KEY IDX_IMPARTE_CURSO (IMP_CUR_ID),
    KEY IDX_IMPARTE_INSTRUCTOR (IMP_INS_ID),

    CONSTRAINT FK_IMPARTE_CURSO
        FOREIGN KEY (IMP_CUR_ID)
        REFERENCES t_curso (CUR_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT FK_IMPARTE_INSTRUCTOR
        FOREIGN KEY (IMP_INS_ID)
        REFERENCES t_instructor (INS_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


-- ============================================================
-- 8. TABLA MATRICULA
-- Relaciona aprendices con cursos
-- ============================================================

CREATE TABLE t_matricula (
    MAT_ID INT NOT NULL AUTO_INCREMENT,
    MAT_UUID VARCHAR(37) NOT NULL,
    MAT_ESTADO VARCHAR(45) NOT NULL,
    MAT_FECHA_INSCRIPCION DATE NOT NULL,
    MAT_APR_ID INT NOT NULL,
    MAT_CUR_ID INT NOT NULL,

    PRIMARY KEY (MAT_ID),

    UNIQUE KEY UK_MATRICULA_UUID (MAT_UUID),

    KEY IDX_MATRICULA_APRENDIZ (MAT_APR_ID),
    KEY IDX_MATRICULA_CURSO (MAT_CUR_ID),

    CONSTRAINT FK_MATRICULA_APRENDIZ
        FOREIGN KEY (MAT_APR_ID)
        REFERENCES t_aprendiz (APR_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT FK_MATRICULA_CURSO
        FOREIGN KEY (MAT_CUR_ID)
        REFERENCES t_curso (CUR_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


-- ============================================================
-- 9. TABLA MAT_EVA
-- Relaciona matrículas con evaluaciones y notas
-- ============================================================

CREATE TABLE t_mat_eva (
    MATE_ID INT NOT NULL AUTO_INCREMENT,
    MATE_UUID VARCHAR(37) NOT NULL,
    MATE_EVA_ID INT NOT NULL,
    MATE_MAT_ID INT NOT NULL,
    MATE_NOTA DECIMAL(3,1) DEFAULT NULL,

    PRIMARY KEY (MATE_ID),

    UNIQUE KEY UK_MAT_EVA_UUID (MATE_UUID),

    KEY IDX_MAT_EVA_EVALUACION (MATE_EVA_ID),
    KEY IDX_MAT_EVA_MATRICULA (MATE_MAT_ID),

    CONSTRAINT FK_MAT_EVA_EVALUACION
        FOREIGN KEY (MATE_EVA_ID)
        REFERENCES t_evaluacion (EVA_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT FK_MAT_EVA_MATRICULA
        FOREIGN KEY (MATE_MAT_ID)
        REFERENCES t_matricula (MAT_ID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;