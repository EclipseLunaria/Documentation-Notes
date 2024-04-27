
To react application that includes *Linting, Unit Testing and code formatting*. You will follow the steps below:

### Creating Typescript React Project
Type the following into the visual studio code terminal
```bash
npx create-react-app {App Name} --template typescript
```

Then reopen visual studio into the new folder created


### Adding Linting
Add ESLint through the extensions manager in vs code

#### Adding code formatting

*install prettier:* `npm i -D prettier`

set prettier as default in overlapping settings with eslint

`npm i -D eslint-config-prettier eslint-plugin-prettier`

then add the config to eslint
```json
{
...,
"eslintConfig":{
	"extends":{
		"react-app",
		"react-app/jest",
		"plugin:prettier/recommend"
		}
	}
}
```


#####  Create prettier config
- Create file called `.prettierrc.json`
- Add the following code for its contents
```json
{
	"printWidth" : 100,
	"singleQuote" : true,
	"semi" : true,
	"tabWidth" : 2,
	"trailingComma" : "all",
	"endOfLine" : "auto"
}
```