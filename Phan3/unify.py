from fact import Fact
from substitution import Substitution

def unify(x, y, theta):
  if theta is False:
    return False
  if (x == y):
    return theta
  if (Fact.is_variable(x)):
    return unifyVar(x, y, theta)
  elif (Fact.is_variable(y)):
    return unifyVar(y, x, theta)
  elif (Fact.is_fact_in_fact(x) and Fact.is_fact_in_fact(y)):
    return unify(x.get_args(), y.get_args(), unify(x.get_op(), y.get_op(), theta))
  elif (Fact.is_list_of_fact(x) and Fact.is_list_of_fact(y)):
    return unify(x[1:], y[1:], unify(x[0], y[0], theta))
  return False

def unifyVar(var, x, theta):
  if (theta.containVar(var)):
    return unify(theta.getValBaseOnVal(var), x, theta)
  elif (theta.containVar(x)):
    return unify(var, theta.getValBaseOnVal(x), theta)
  
  theta.add(var, x)
  return theta
