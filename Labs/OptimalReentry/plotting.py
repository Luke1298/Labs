from __future__ import division
from math import pi, sqrt, sin, cos, exp
from numpy import linspace, array, tanh, cosh, ones, arctan
import numpy as np
from scipy.special import erf
from scikits import bvp_solver
import matplotlib.pyplot as plt


def reentry_init(plot=False):
	R = 209
	beta = 4.26
	rho0 = 2.704e-3
	g = 3.2172e-4
	s = 26600		# 53200;
	T_init = 230
	
	p1, p2, p3 = 1.6, 4, .5	# 1.09835, 6.48578, .347717
	
	x_array = linspace(0,T_init,100) 
	plt.plot(x_array,p1*erf( p2*(p3-x_array/T_init) ),'-k',linewidth=2.0) 
	plt.show()
	plt.clf()
	
	#############################################################
	def guess_auxiliary(x):
		out = array([ .5*(.36+.27)-.5*(.36-.27)*tanh(.025*(x-.45*T_init)),
			pi/180*(.5*(-8.1 + 0)-.5*(-8.1 - 0)*tanh(.025*(x-.25*T_init)) ), # pi/180*
			(1/R)*( .5*(4+2.5)-.5*(4-2.5)*tanh(.03*(x-.3*T_init)) - 
			1.4*cosh(.025*(x-.25*T_init))**(-2) ), # (1/R)*
			p1*ones(x.shape),
			p2*ones(x.shape),
			p3*ones(x.shape)   ])
		return out
	
	#############################################################
	def F(x,y):
		u =	 arctan((6*y[4])/(9*y[0]*y[3] ))
		rho = rho0*exp(-beta*R*y[2])
		out = y[6]*array([
				 -s*rho*y[0]**2*C_d(u) - g*sin(y[1])/(1+y[2])**2,        # F_1
				( s*rho*y[0]*C_l(u) + y[0]*cos(y[1])/(R*(1 + y[2])) - 
				  g*cos(y[1])/(y[0]*(1+y[2])**2) ),						 # F_2
				y[0]*sin(y[1])/R,										 # F_3
				-( 30*y[0]*sqrt(rho)+ y[3]*(-s*rho*y[0]*C_d(u)) + 
				   y[4]*( s*rho/2*C_l(u) +cos(y[1])/(R*(1 + y[2])) + 
				   		  g*cos(y[1])/( y[0]**2*(1+y[2])**2 ) 
				   	   		) + 
				   y[5]*(sin(y[1])/R)	   ),							 # F_4
				-( y[3]*( -g*cos(y[1])/(1+y[2])**2	) + 
			   	   y[4]*( -y[0]*sin(y[1])/(R*(1+y[2])) + 
					   	  g*sin(y[1])/(y[0]*(1+y[2])**2 ) 
					   		) + 
			   	   y[5]*(y[0]*cos(y[1])/R )	   ),						 # F_5
			   		'6th entry', 
					0 # T' = 0
			   ])
		return out

	#############################################################
	def F_auxiliary(x,y):
		u = y[3]*erf( y[4]*(y[5]-x/T_init) )
		rho = rho0*exp(-beta*R*y[2])
		out = array([-s*rho*y[0]**2*C_d(u) - g*sin(y[1])/(1+y[2])**2,
					  ( s*rho*y[0]*C_l(u) + y[0]*cos(y[1])/(R*(1 + y[2])) - 
					  g*cos(y[1])/(y[0]*(1+y[2])**2) ),
					  y[0]*sin(y[1])/R,
					  0,
					  0,
					  0		])
		return out
	
	#############################################################
	def bc2_auxiliary(ya,yb):
		# out = array([ ya[0]-.36,
		#			  ya[1]+8.1*pi/180,
		#			  ya[2]-4/R,
		#			  yb[0]-.27,
		#			  yb[1],
		#			  yb[2]-2.5/R
		#			  ])
		# return out
		
		out1 = array([ ya[0]-.36,
					  ya[1]+8.1*pi/180,
					  ya[2]-4/R
					  ])
		out2 = array([ yb[0]-.27,
					  yb[1],
					  yb[2]-2.5/R
					  ])
		return out1, out2
	
	#############################################################
	def bc2(ya,yb):
		out1 = array([ ya[0]-.36,
					  ya[1]+8.1*pi/180,
					  ya[2]-4/R
					  ])
					 
		out2 = array([yb[0]-.27,
					  yb[1],
					  yb[2]-2.5/R,
					  H(yb)
					  ])
		return out1, out2
	
	#############################################################
	def H(y):
		# alpha = sqrt((.6*y[4])^2 + (.9*y[0]*y[3])^2)
		# sin(u) = -.6*y[4]/alpha
		# cos(u) = -.9*y[0]*y[3]/alpha
		# tan(u) = (6*y[4])/(9*y[0]*y[3] )

		u =	 atan((6*y[4])/(9*y[0]*y[3] )) 
		rho = rho0*exp(-beta*R*y[2])

		out = (10*y[0]**3*sqrt(rho) + 
					y[3]*(-s*rho*y[0]**2*C_d(u) - g*sin(y[1])/(1+y[2])**2 ) + 
					y[4]*(  s*rho*y[0]*C_l(u) + y[0]*cos(y[1])/(R*(1 + y[2])) - 
							g*cos(y[1])/(y[0]*(1+y[2])**2)
							) + 
					y[5]*y[0]*sin(y[1])/R
				)
		return out
	
	#############################################################
	def C_d(u):
		return 1.174 - 0.9*cos(u)

	def C_l(u):
		return 0.6*sin(u)

	def u(x):
		return p1*erf( p2*(p3-x/T_init) )



	auxiliary_problem = bvp_solver.ProblemDefinition(num_ODE = 6,
										  num_parameters = 0,
										  num_left_boundary_conditions = 3,
										  boundary_points = (0., T_init),
										  function = F_auxiliary,
										  boundary_conditions = bc2_auxiliary)
									
	auxiliary_solution = bvp_solver.solve(auxiliary_problem,
								solution_guess = guess_auxiliary)
	
	# plt.rc("font", size=16)
	
	# x0 = linspace(0,T_init,120)
	# y0 = guess_auxiliary(x0)
	# plt.plot(x0,y0[1,:],'-k',linewidth=2.0)
	# plt.ylabel('$v$'); plt.show(); plt.clf()
	#
	# plt.plot(x0,180/pi*y0[2,:],'-b',linewidth=2.0)
	# plt.ylabel('$\gamma$'); plt.show(); plt.clf()
	#
	# plt.plot(x0,R*y0[3,:],'-g',linewidth=2.0)
	# plt.ylabel('$h$'); plt.show(); plt.clf()


	# xint = linspace(0,T_init,120)
	# yint = solution(xint)
	# g = guess_auxiliary(xint)
	# for j in range(3):
	# 	plt.plot(xint,np.real(yint[j,:]),'-k',linewidth=2.0)
	# 	plt.plot(xint,g[j,:],'-r',linewidth=2.0)
	# plt.xlabel('$x$')
	# plt.ylabel('$y$')
	# plt.show()
	
	if plot==True:
		xint = linspace(0,T_init,120)
		yint = auxiliary_solution(xint)
		# Plot guess for v
		plt.plot(xint,np.real(yint[0,:]),'-k',linewidth=2.0)
		plt.xlabel('$t$',fontsize=18); plt.ylabel('$v$',fontsize=18)
		plt.savefig('guess_v.pdf')
		plt.show(); plt.clf()
		
		# Plot guess for gamma
		plt.plot(xint,np.real(yint[1,:]),'-k',linewidth=2.0)
		plt.xlabel('$t$',fontsize=18); plt.ylabel(r'$\gamma$',fontsize=18)
		plt.savefig('guess_gamma.pdf')
		plt.show(); plt.clf()
		
		# Plot guess for xi
		plt.plot(xint,np.real(yint[2,:]),'-k',linewidth=2.0)
		plt.xlabel('$t$',fontsize=18); plt.ylabel(r'$\xi$',fontsize=18)
		plt.savefig('guess_xi.pdf')
		plt.show(); plt.clf()
		
		# Plot guess for control u
		p1, p2, p3 = yint[3,0], yint[4,0], yint[5,0]
		plt.plot(xint,p1*erf( p2*(p3-xint/T_init) ),'-k',linewidth=2.0)
		plt.xlabel('$t$',fontsize=18); plt.ylabel(r'$u$',fontsize=18)
		plt.savefig('guess_u.pdf')
		plt.show(); plt.clf()
	
	
	
	xint = linspace(0,T_init,120)
	yint = auxiliary_solution(xint)
	yint = np.concatenate( (yint,T_init*np.ones((1,120))) ,axis=0)
	# print yint.shape, yint.dtype
	
	original_problem = bvp_solver.ProblemDefinition(num_ODE = 7,
										  num_parameters = 0,
										  num_left_boundary_conditions = 3,
										  boundary_points = (0., 1),
										  function = F_auxiliary,
										  boundary_conditions = bc2_auxiliary)
									
	original_solution = bvp_solver.solve(original_problem,
								solution_guess = yint,
								initial_mesh = xint)
	# # For more info on the available options for these methods, run
	# print bvp_solver.ProblemDefinition.__doc__
	# print bvp_solver.solve.__doc__
	
	
	
	return auxiliary_solution
	











def bvp_solver_example():
	""" 
	Using scikits.bvp_solver to solve the bvp
	"""
	epsilon = .1
	lbc, rbc = 0., 1.
	
	def function1(x , y):
		return np.array([y[1] , (4./epsilon)*(pi-x**2.)*y[0] + 1./epsilon*np.cos(x) ]) 
	
	
	def boundary_conditions(ya,yb):
		return (np.array([ya[0] - lbc]), 
				np.array([yb[0] - rbc]))
	
	problem = bvp_solver.ProblemDefinition(num_ODE = 2,
										  num_parameters = 0,
										  num_left_boundary_conditions = 1,
										  boundary_points = (0., pi/2.),
										  function = function1,
										  boundary_conditions = boundary_conditions)
									
	solution = bvp_solver.solve(problem,
								solution_guess = (1.,
												  0.))
											
	A = np.linspace(0.,pi/2., 200)
	T = solution(A)
	plt.plot(A, T[0,:],'-k',linewidth=2.0)
	plt.show()
	plt.clf()
	return


if __name__ == "__main__":
	# bvp_solver_example()
	reentry_init()



