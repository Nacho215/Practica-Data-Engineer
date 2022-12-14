USE [master]
GO
/****** Object:  Database [unidad13]    Script Date: 4/11/2022 15:13:07 ******/
CREATE DATABASE [unidad13]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'unidad13', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\unidad13.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'unidad13_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\unidad13_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [unidad13] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [unidad13].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [unidad13] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [unidad13] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [unidad13] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [unidad13] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [unidad13] SET ARITHABORT OFF 
GO
ALTER DATABASE [unidad13] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [unidad13] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [unidad13] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [unidad13] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [unidad13] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [unidad13] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [unidad13] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [unidad13] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [unidad13] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [unidad13] SET  ENABLE_BROKER 
GO
ALTER DATABASE [unidad13] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [unidad13] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [unidad13] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [unidad13] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [unidad13] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [unidad13] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [unidad13] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [unidad13] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [unidad13] SET  MULTI_USER 
GO
ALTER DATABASE [unidad13] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [unidad13] SET DB_CHAINING OFF 
GO
ALTER DATABASE [unidad13] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [unidad13] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [unidad13] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [unidad13] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [unidad13] SET QUERY_STORE = OFF
GO
USE [unidad13]
GO
/****** Object:  Table [dbo].[Alumno]    Script Date: 4/11/2022 15:13:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Alumno](
	[legajo] [int] NOT NULL,
	[nombre] [varchar](45) NOT NULL,
	[apellido] [varchar](45) NOT NULL,
	[fecha_nacimiento] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[legajo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cursa]    Script Date: 4/11/2022 15:13:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cursa](
	[legajo] [int] NULL,
	[codigo] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Materia]    Script Date: 4/11/2022 15:13:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Materia](
	[codigo] [int] NOT NULL,
	[descripcion] [varchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Alumno] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (3235, N'Juan Ignacio', N'Hernández', CAST(N'1997-05-21' AS Date))
INSERT [dbo].[Alumno] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (3784, N'Belén', N'Tapia', CAST(N'1995-01-09' AS Date))
INSERT [dbo].[Alumno] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (4233, N'Pedro', N'Álvarez', CAST(N'1995-08-15' AS Date))
INSERT [dbo].[Alumno] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (4421, N'Camila', N'Morales', CAST(N'1999-11-24' AS Date))
INSERT [dbo].[Alumno] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (4563, N'Martín', N'Ledesma', CAST(N'1996-04-03' AS Date))
GO
INSERT [dbo].[Cursa] ([legajo], [codigo]) VALUES (3784, 1)
INSERT [dbo].[Cursa] ([legajo], [codigo]) VALUES (3235, 4)
INSERT [dbo].[Cursa] ([legajo], [codigo]) VALUES (4563, 3)
INSERT [dbo].[Cursa] ([legajo], [codigo]) VALUES (4563, 5)
INSERT [dbo].[Cursa] ([legajo], [codigo]) VALUES (3784, 2)
GO
INSERT [dbo].[Materia] ([codigo], [descripcion]) VALUES (1, N'Matemáticas')
INSERT [dbo].[Materia] ([codigo], [descripcion]) VALUES (2, N'Física')
INSERT [dbo].[Materia] ([codigo], [descripcion]) VALUES (3, N'Química')
INSERT [dbo].[Materia] ([codigo], [descripcion]) VALUES (4, N'Programación')
INSERT [dbo].[Materia] ([codigo], [descripcion]) VALUES (5, N'Psicología')
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD FOREIGN KEY([codigo])
REFERENCES [dbo].[Materia] ([codigo])
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD FOREIGN KEY([legajo])
REFERENCES [dbo].[Alumno] ([legajo])
GO
USE [master]
GO
ALTER DATABASE [unidad13] SET  READ_WRITE 
GO
