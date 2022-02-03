#loading libraries
library(tidyverse)
library(magrittr)
library(lubridate)

#reading original data
datos <- read.csv("./Casos_positivos_de_Covid-19_en_el_departamento_de_Antioquia.csv") # nolint

area <- c("MEDELLIN", "ITAGUI", "BELLO", "GIRARDOTA", "CALDAS",
"ENVIGADO", "SABANETA", "LA ESTRELLA", "COPACABANA", "BARBOSA") #metropolitan area municiples # nolint
#cleaning data
datos %<>%
    select(Fecha.de.recuperación, Nombre.municipio, Recuperado, Fecha.de.muerte) %>% # nolint selecting necessary variables to build the data base for modelling
    mutate(Fecha.de.recuperación = str_extract(Fecha.de.recuperación, "\\d+-\\d+-\\d+"), # nolint
    Fecha.de.recuperación = as.Date(Fecha.de.recuperación), #formatting dates
    Fecha.de.muerte = str_extract(Fecha.de.muerte, "\\d+-\\d+-\\d+"),
    Fecha.de.muerte = as.Date(Fecha.de.muerte), #formatting dates
    Recuperado = if_else(Recuperado == "fallecido", "Fallecido", Recuperado)) %>% #properly formatting data # nolint
    filter(Recuperado %in% c("Recuperado", "Fallecido")) %>%
    mutate(Fecha = if_else(Recuperado == "Recuperado", Fecha.de.recuperación, Fecha.de.muerte), # nolint
    Mes = month(Fecha), Anio = year(Fecha)) %>% #creating proper date variable # nolint
    select(Mes, Anio, Recuperado, Nombre.municipio) %>%
    filter(Nombre.municipio %in% area) %>%
    arrange(Mes, Anio)

final_data <- datos %>%
    group_by(Anio, Mes, Nombre.municipio) %>%
    summarise(
    Recuperados = sum(Recuperado != "Fallecido"),
    Cuarentena = if_else(Anio > 2020, "No", if_else(Mes >= 10, "No", "Si")), # nolint
    Vacunacion = if_else(Anio == 2020, "No", if_else(Mes >= 2, "Si", "No")),
    Post_vacaciones = if_else(Mes %in% c(7, 1), "Si", "No"))

final_data <- final_data[!duplicated(final_data), ]
saveRDS(final_data, "Data.Rds")
