SRC += side.c
SRC += rf.c
SRC += sleep.c
SRC += rf_driver.c
UART_DRIVER_REQUIRED   = yes
RGB_MATRIX_CUSTOM_USER = yes

ifeq ($(strip $(NUPHY_BATTERY_TELEMETRY)),yes)
    OPT_DEFS += -DNUPHY_BATTERY_TELEMETRY
endif
