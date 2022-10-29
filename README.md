# Hydrangea 💐

Newest data api for hydroponics.

## Contribute

To setup, make sure you have python and pip installed.

Instantiate a [virtual environment](https://docs.python.org/3/library/venv.html) named venv if the venv folder does not exist. Make sure you activate it.

Download [Mongodb](https://www.mongodb.com/docs/manual/administration/install-community/) and optionally mongosh.

Create a .env file with a database URL. To store database locally, add:
` MONGODB_URL=mongodb://localhost:27017/test`

To Run API from root directory, run

```
python3 app/main.py
```

# Schema

This is the schema layed out for the api to organize the various sensors and actuators, as well as recording actions and readings

### Sensor

| Name       | Type          |
| ---------- | ------------- |
| id         | `Key`         |
| name       | `String`      |
| garden_id  | `Foreign Key` |
| created_at | `Datetime`    |

### Scheduled Actuators

| Name       | Type          |
| ---------- | ------------- |
| id         | `Key`         |
| name       | `String`      |
| garden_id  | `Foreign Key` |
| created_at | `Datetime`    |

### Reactive Actuators

| Name       | Type          |
| ---------- | ------------- |
| id         | `Key`         |
| name       | `String`      |
| sensor_id  | `Foreign Key` |
| created_at | `Datetime`    |

### Gardens

| Name       | Type       |
| ---------- | ---------- |
| id         | `Key`      |
| name       | `String`   |
| location   | `String`   |
| created_at | `Datetime` |

# Logging

We will also keep track of the actions that actually took place and readings taken from sensors.

### Readings

| Name       | Type          |
| ---------- | ------------- |
| id         | `Key`         |
| name       | `String`      |
| sensor_id  | `Foreign Key` |
| value      | `Float`       |
| created_at | `Datetime`    |

### Scheduled Actions

| Name       | Type          |
| ---------- | ------------- |
| id         | `Key`         |
| name       | `String`      |
| actuator   | `Foreign Key` |
| data       | `String`      |
| created_at | `Datetime`    |

### Reactive Actions

| Name       | Type          |
| ---------- | ------------- |
| id         | `Key`         |
| name       | `String`      |
| actuator   | `Foreign Key` |
| data       | `String`      |
| created_at | `Datetime`    |

# Config

The Configurations Table will be used in conjunction with logging data in [Mother Nature](https://github.com/Olin-Hydro/mother-nature)

### Operational Config File

| Name                | Type           |
| ------------------- | -------------- |
| id                  | `Key`          |
| garden_id           | `Foreign Key`  |
| name                | `String`       |
| sensors             | `SensorConfig` |
| scheduled_actuators | `SAConfig`     |
| reactive_actuators  | `RAConfig`     |
| created_at          | `Datetime`     |

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
| GET  | `/sensors/logging/`                 | `view all sensor readings`                       |
| GET  | `/sensors/logging/:sensorId`        | `view all readings for a specific sensor`        |
| GET  | `/sensors/logging/:sensorId/recent` | `view most recent reading for a specific sensor` |
| POST | `/sensors/logging/`                 | `add sensor reading`                             |

### Reactive Actions

| Verb | URI Pattern                     | Controller Action      |
| ---- | ------------------------------- | ---------------------- |
| GET  | `/ra/logging/actions/`          | `view all actions`     |
| GET  | `/ra/logging/actions/:actionId` | `view specific action` |
| POST | `/ra/logging/actions/`          | `add actions`          |

### Scheduled Actions

| Verb | URI Pattern                     | Controller Action      |
| ---- | ------------------------------- | ---------------------- |
| GET  | `/sa/logging/actions/`          | `view all actions`     |
| GET  | `/sa/logging/actions/:actionId` | `view specific action` |
| POST | `/sa/logging/actions/`          | `add actions`          |
