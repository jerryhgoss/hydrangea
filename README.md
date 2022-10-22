# Hydrangea 💐

Newest data api for hydroponics.

# Schema

This is the schema layed out for the api to organize the various sensors and actuators, as well as recording actions and readings

### Sensor

| Name       | Type          |
| ---------- | ------------- |
| Id         | `Key`         |
| Name       | `String`      |
| Garden_Id  | `Foreign Key` |
| Interval   | `Float`       |
| Created_at | `Timestamp`   |

### Scheduled Actuators

| Name       | Type          |
| ---------- | ------------- |
| Id         | `Key`         |
| Name       | `String`      |
| Garden_Id  | `Foreign Key` |
| On_times   | `[str]`       |
| Off_times  | `[str]`       |
| Created_at | `Timestamp`   |

### Reactive Actuators

| Name       | Type          |
| ---------- | ------------- |
| Id         | `Key`         |
| Name       | `String`      |
| Garden_Id  | `Foreign Key` |
| Sensor     | `Foreign Key` |
| Threshold  | `Float`       |
| Created_at | `Timestamp`   |

### Gardens

| Name       | Type        |
| ---------- | ----------- |
| Id         | `Key`       |
| Name       | `String`    |
| locations  | `String`    |
| Created_at | `Timestamp` |

# Logging

We will also keep track of the actions that actually took place and readings taken from sensors.

### Readings

| Name       | Type          |
| ---------- | ------------- |
| Id         | `Key`         |
| Name       | `String`      |
| Garden_Id  | `Foreign Key` |
| Sensor_Id  | `Foreign Key` |
| Value      | `Float`       |
| Created_at | `Timestamp`   |

### Scheduled Actions

| Name       | Type          |
| ---------- | ------------- |
| Id         | `Key`         |
| Name       | `String`      |
| Garden_Id  | `Foreign Key` |
| Type       | `str`         |
| Data       | `str`         |
| Created_at | `Timestamp`   |

### Reactive Actions

| Name       | Type          |
| ---------- | ------------- |
| Id         | `Key`         |
| Name       | `String`      |
| Garden_Id  | `Foreign Key` |
| Type       | `str`         |
| Data       | `str`         |
| Created_at | `Timestamp`   |

# Config

The Configurations Table will be used in conjunction with logging data in [Mother Nature](https://github.com/Olin-Hydro/mother-nature)

### Config File

| Name                   | Type            |
| ---------------------- | --------------- |
| Id                     | `Key`           |
| Garden_Id              | `Foreign Key`   |
| Sensor_ids             | `[Foreign Key]` |
| Scheduled_actuator_ids | `[Foreign Key]` |
| Reactive_actuator_ids  | `[Foreign Key]` |
| Created_at             | `Timestamp`     |

<hr />

# Route Tables

### Sensors

| Verb   | URI Pattern          | Controller Action        |
| ------ | -------------------- | ------------------------ |
| GET    | `/sensors/`          | `view all sensors`       |
| GET    | `/sensors/:sensorId` | `view individual sensor` |
| POST   | `/sensors/`          | `add`                    |
| PATCH  | `/sensor/:sensorId`  | `update`                 |
| DELETE | `/sensor/:sensorId`  | `destroy`                |

### Scheduled Actuators

| Verb   | URI Pattern | Controller Action              |
| ------ | ----------- | ------------------------------ |
| GET    | `/sa/`      | `view all scheduled actuators` |
| GET    | `/sa/:saId` | `view scheduled actuators`     |
| POST   | `/sa/`      | `add`                          |
| PATCH  | `/sa/:saId` | `update`                       |
| DELETE | `/sa/:saId` | `destroy`                      |

### Reactive Actuators

| Verb   | URI Pattern | Controller Action             |
| ------ | ----------- | ----------------------------- |
| GET    | `/ra/`      | `view all reactive actuators` |
| GET    | `/ra/:raId` | `view reactive actuators`     |
| POST   | `/ra/`      | `add`                         |
| PATCH  | `/ra/:raId` | `update`                      |
| DELETE | `/ra/:raId` | `destroy`                     |

<hr />

### Gardens

| Verb   | URI Pattern          | Controller Action                     |
| ------ | -------------------- | ------------------------------------- |
| GET    | `/gardens/`          | `view all gardens`                    |
| GET    | `/gardens/:gardenId` | `view readings for a specific garden` |
| POST   | `/gardens/`          | `add`                                 |
| PATCH  | `/gardens/:gardenId` | `update`                              |
| DELETE | `/gardens/:gardenId` | `destroy`                             |

<hr />

## Logging

### Sensor

| Verb | URI Pattern                         | Controller Action                                |
| ---- | ----------------------------------- | ------------------------------------------------ |
| GET  | `/logging/sensors/`                 | `view all sensor readings`                       |
| GET  | `/logging/sensors/:sensorId`        | `view all readings for a specific sensor`        |
| GET  | `/logging/sensors/:sensorId/recent` | `view most recent reading for a specific sensor` |
| POST | `/logging/sensors/`                 | `add sensor reading`                             |

### Actions

| Verb | URI Pattern                 | Controller Action      |
| ---- | --------------------------- | ---------------------- |
| GET  | `/logging/actions/`         | `view all actions`     |
| GET  | `/logging/actions/actionId` | `view specific action` |
| POST | `/logging/actions/`         | `add actions`          |
