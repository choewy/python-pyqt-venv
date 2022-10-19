# python-pyqt6-venv

## Step

```
$ npm i
```

### Install Python3.10 for Mac(brew)

```
$ npm run install:python
```

### Activate venv(create venv if not exists)

```
$ npm run venv
```

### Install venv dependencies

```
(venv) npm run install:package
```

### Run python3(with nodemon)

```
(venv) npm run start
```

## Environment

- `./.env.json`

```ts
{
  version: string;
}
```

## Other

### Freeze venv dependencies

```
(venv) npm run freeze
```

### Uninstall venv dependencies

```
(venv) npm run uninstall:package
```
