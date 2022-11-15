my_python_version=$(python -V)
if [[ $my_python_version = *$0* ]];then
  echo "✅ Python verzija OK."
else
  echo "❌ Python verzija je $my_python_version a treba da bude $0."
fi
