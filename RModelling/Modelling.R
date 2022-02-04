library(lme4)
library(tidyverse)
datos <- readRDS("./Data.Rds")
datos_temp <- datos
datos_temp[, c("Anio", "Mes")] <- scale(datos_temp[, c("Anio", "Mes")])
modnull <- glmer(Recuperados ~ 1 + (1 | Nombre.municipio), data = datos, family = poisson()) # nolint
modone <- glmer(Recuperados ~  Anio + (1 | Nombre.municipio), data = datos, family = poisson()) # nolint
modtwo <- glmer(Recuperados ~ Anio + Mes + (1 | Nombre.municipio), data = datos, family = poisson()) # nolint
modthree <- glmer(Recuperados ~ Anio + Mes + (Mes | Nombre.municipio), data = datos, family = poisson()) # nolint
modfour <- glmer(Recuperados ~ Anio + Mes + Vacunacion + (Mes | Nombre.municipio), data = datos, family = poisson()) # nolint
modfive <- glmer(Recuperados ~ Anio + Mes + Vacunacion + Cuarentena + Post_vacaciones + (Cuarentena + Mes | Nombre.municipio), data = datos, family = poisson()) # nolint
anova(modnull, modone)
anova(modone, modtwo)
anova(modtwo, modthree)
anova(modthree, modfour)
anova(modfour, modfive)
datos$Recuperados_hat <- round(predict(modfive, type = "response")) # nolint
View(datos)
datos_to_vis <- data.frame(Anio = rep(datos$Anio, 2),
    Mes = rep(datos$Mes, 2), Recuperados = c(datos$Recuperados, datos$Recuperados_hat), # nolint
    Clase = rep(c("Real", "Predicho"), each = nrow(datos)),
    Municipio = rep(datos$Nombre.municipio, 2))
View(datos_to_vis)

foo <- function(df, anio, municipio) {
    df <- df %>%
        filter(Anio == anio, Municipio == municipio)

    p <- ggplot(df, aes(Mes, Recuperados)) +
    geom_path(aes(color = Clase))

    return(p)
}

temp <- foo(datos_to_vis, 2021, "MEDELLIN")
temp
