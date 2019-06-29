# n-dimensional-pendulum-numerical-analysis
This project was for Advance Computational Mathematics (MATH3976) at the University of Sydney. It was a project based on the exploration of numerical analysis of a N-dimensional pendulum system.

## Content
- Dynamics of a 10-chain system
- Varying the number of masses in the system
- Varying initial conditions of the system
- Analysing the maximum chain energy of the system
- Distribution of Angles
- Statistically Steady State Analysis
- Return Time

## Dynamics of a 10-chain system
This section is an introductory and explarotory look of the pendulum system with 10 mass points in order to understand the baseline behaviour of the system.

### Observations

#### Positions of the chain

We analysed the behaviour of the x and z position of the chain at different points on the chain. We fix the chain to contain 10 mass points. There is a noticable behaviour of the x-position of the chain with that of the cosine function. Furthermore, it is interesting to see that as you go down the chain and observe the x-position behaviour over time, there is notable increase in the amplitude of the x-position further down the chain you go.
![Image](./resources/61956B27AB2CA4815DEDD3F1A52AA11B.jpg =600x270)

With regards to the z-position of the chain, there is a clear decrease in the amplitude over time. This mirrors the physical phenomena of the chain swinging and reaching a lower height as time goes on, hence indicating sanity in the model we have constructed. Here, as in the case with the x-position, the lower down the chain we go, the large the amplitude of the system. Finally, consulting the literature, the first 30 seconds of the graph mirrors what would be generally be seen in a pendulum model, before our model displays unusual behaviour.
![Image](./resources/5746991D8EEF9CD7B14FBE6789F5F725.jpg =600x293)

Comparing the x and z position behaviours, there appears to be an inverse relationship between the x and z position of the pendulum. This can be rationalised as due to the constraints on the system, as we move away from the fixed point in the z-position, this will leads to the pendulum moving closer to the fixed point in the x-position.
![Image](./resources/22A9787196C7A5170D8BC2F323881877.jpg =650x210)
![Image](./resources/6E394742AAEF7BC12D4B26D20D55C835.jpg =650x203)
![Image](./resources/62AA40DA422DCBD5B6069D6BB4990B00.jpg =650x209)

#### Velocity

We attempted to examine the properties of the velocity of the system but looking at the figures below, there appears to be no indicative pattern/trends in the data. However, it is worth noting that the lower down the pendulum you go, the more erratic the behaviour of the velocity.
![Image](./resources/EBD7F443BE5C10F6799F072F104F1BAD.jpg =650x253)
![Image](./resources/BF73B6C1580209E9AA9A67D7C5371B56.jpg =650x281)

Furthermore, looking at the differentiated end points, we do not see any worthwhile patterns to explore.
![Image](./resources/9D3E0B724EBEC181B800E836D445543D.jpg =650x199)
![Image](./resources/FFF6A9BB03E2C7ECD9C09B5444F9F897.jpg =650x192)
![Image](./resources/91BB1E70F9681768849082BE0A790CBE.jpg =650x199)

#### Energy
We examine the energy of the chain over time, which remained largely stationary. This is to be expected due to the conservation of energy in the model. However, there is a noticeable point in time where we see a sharp increase in the energy of the system. Upon review, this is attributable to the "snap" of the chain. Leaving the system to run for longer did not see any other instances of "snaps" and resultantly, means of predicting the next "snap" of the chain.
![Image](./resources/A34CA3B80FA562D9B3B24CDE9190C637.jpg =450x400)

## Varying the number of masses in the system
We looked the varying the number of masses in the system and how does it affect the factors mentioned in the aforementioned section.
### Observations

#### Position
We examined 3 instances where we had the number of masses be either 4, 40, or 400. It is extremely interesting to note that as n increases, we see a _smoothing_ of the graph and a clearer cosine behaviour is observed. This is attributable to the fact that as n increases, we are increasing the chain length, and resultantly, the frequency decreases, with the period increasing. We display only the plots for n=4 and n=400. Please refer to the appendix in section 2.1 for further graphs.

![Image](./resources/9FF39E1E8A8801BE6B471A6425F43B50.jpg =700x150)
![Image](./resources/E25ECD47B57BFD625384459AFF535762.jpg =700x150)
![Image](./resources/608B4EC1A76B936A849D5DD9A8886A89.jpg =700x150)
![Image](./resources/D1A837856F0B6E6A6D5C52E507BEB4D1.jpg =700x150)
#### Velocity
We see a similar scenario for velocity that as n increases, we see a smoothing out of the graphs. Please refer to appendix section 2.2 for the graphs of the velocity.

#### Energy
Regarding the energy, we again see a smoothing out effect for a larger N, such that the conservation of energy is distinct. Furthermore, the energy spike from the snap is even more pronounced and it is interesting to note that the energy level post snap is actually at a lower level compared to pre-snap. Please refer to the appendix section 2.3 for the graphs of the n=4 and 40 scenario.
![Image](./resources/CCF107C959DD70058A05927737FEE3CB.jpg =500x400)

## Varying initial conditions of the system
In this section, we look to vary the initial conditions of the system and see the effects of this on position, velocity, and energy of the system.
### Data
We selected 3 different initial conditions for a chain of size 4 as seen in the plot below. The highest initial condition will see the chain being released from a more curved orientation whilst the lowest initial condition will have a lower center of mass due to it being released from a lesser curvature.
![Image](./resources/A7AC4A73A384E2638D05C40576B61613.jpg =350x289)

### Observations
#### Position
Please refer to appendix section 3.1 for the graphs of the positions starting from different initial conditions. It is evidently seen that as we start the chain off from a straighter orientation and lower center of mass, we see a consistent behaviour of the chain's position, exhibiting behaviours similar to that of a sine wave. The more curved the orientation of the initial position, we see much more erratic behaviour in the system. This is consistent with theory of pendulums whereby as we analyse the system with higher angles $\theta$, the system becomes much more erratic. It is also worth noting that the amplitude of the waves decreases at different parts of the chain yet they still reach the nodal and antinodal positions in space in the same time period.

#### Velocity
Please refer to appendix section 3.2 for the graphs of the velocity of the chain from different initial conditions. 
As mentioned in the subsection of the position of the chain, we see a similar effect regarding the smoothing and stable nature of the graphs as we set an initial condition with less curvature.

#### Energy
Please refer to appendix section 3.3 for the graphs of the energy of the chain from different initial conditions. 
The energy of the system exhibits a decreasing trend with time which, considering that the energy is always negative and could be representative of gravitational potential energy, appears to break the Law of Conservation of Energy. This suggests multiple issues with the model.

## Analysing the maximum chain energy of the system
We analyse the maximum energy reached in the system resulting from the "snap" of the chain.

### Data
We look at two different initial conditions and see the effect of them on the "snap" of the chain and hence the maximum amount of energy reached in the system. We contrast the settings of where the initial condition is from a vertical position and the initial condition is from a horizontal position. Please refer to the figures below for an illustration of what is meant.
![Image](./resources/CFE2096D95DA3C59828FC85FB7B41C1C.jpg =250x150)
![Image](./resources/7B3740F41C00C8250DD66290354D3D5A.jpg =250x150)

### Observation
The first figure below showcases the energy of the system from an vertical initial condition whilst the second figure is of the energy of the system from a horizontal initial condition. The energy from the vertical initial position has significantly higher energy than the other condition, which makes intuitive sense as there is more potential energy in the system. Furthermore, the vertical initial position system exhibits larger fluctuations in the energy, with a standard deviation of 0.1 compared to 0.02 in the horizontal initial position. This indicates of chain snaps with higher energy, which are more significant in latter time periods after the release of the chain. This indicates that the chain was flung higher into the air following a snap and is related to the larger positive fluctuations of energy seen in the horizontal chain system.

![Image](./resources/EE44414CF70FEBC4960FCA0F52FAC07D.jpg =500x350)
![Image](./resources/C9A2993A917B259AE8A74F96C7757A00.jpg =500x350)

## Distribution of angles
We look at the distribution of angles in the system after a certain time point T. The rationale being that after T, the system would "stabilise" to some extent. We are interested in analysing the distribution of angles of the masses in this stabilised setting.

### Data
Here we are interested in what does the empirical distribution of the angles of pendulum look like after the system has supposedly "stabilised". In this setting, we defined this stability to be after a long prolonged period of time. From this, we can plot the histogram of the distribution of angles. Additionally, we can plot the Empircal Cumulative Distribution Function (ECDF) of the data. The ECDF is an estimate of the cumulative distribution function that generated the points in the sample. If the conditions are satisfied, the ECDF converges with probability 1 to the underlying distribution, according to the [Glivenko–Cantelli theorem](https://en.wikipedia.org/wiki/Glivenko%E2%80%93Cantelli_theorem). We then run the nonparametric test [Kolmogorov Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) for equality of the empirical distribution function to the proposed cumulative distribution function, which in the case we chose the Gaussian distribution function. If Glivenko-Cantelli holds, and the data is drawn from a random variable with a Gaussian distribution, then the Kolmogorov-Smirnov test should indicate equality of ECDF and proposed Gaussian CDF.

### Observations
We display the histogram and empirical cumulative distribution function for mass 1 and 10. Please refer to appendix 5.1 for the graphs of the other masses.

![Image](./resources/08FE7E9F9C42A3E12A4AAF156ED19739.jpg =350x300)
![Image](./resources/CE97E98E65F705BADC9205CDEE23C81D.jpg =350x300)


Unforuntately, according to the Kolmogorov Smirnov test does not indicate that the data is not from a random variable with a Gaussian distribution. All 10 masses indicates this. However, the reader of this report may simply alter and pass in a different proposed distribution in the first line of the `km_test` function to test for different distribution. 

It is interesting to note that the histogram looks different for the angles of the different masses, that is, the angles differ for each of the mass. There are some masses with no "negative" angles, that is, angles where the pendulum has shifted over to the left side of the line going towards the ground. In particular, the first few masses have mainly positive angles and then we see a peak of negative angles for mass 8 before falling back down slowly. 

## Statistically Steady State Analysis
### Data
Here, we investigate the property of the system after a prolonged period of time when the system has supposedly calmed down. We look at the 100 time step moving average for each angle for a fixed time interval and compare the evolutions of 100 time step moving averages for each mass' angle.

### Observations
![Image](./resources/E9F5460F2990CCCBAF2EAF987C829519.jpg =400x400)
![Image](./resources/31008923DA90E54B7EE927658FC9626C.jpg =400x400)
It is clear hear that there are periodic swings in the 100 time step moving average of the velocity and angle for mass 10.

## Return Time

### Data
We look at the time periods in which the pendulum returns to its initial state, which we define to be the difference of the sum of angles less the sum of the initial angles to be less than a certain threshold. We vary the number of chains in the system to see how does the return time differ.

### Observations
We display only the return times for a pendulum with 10 masses and one with 70 masses. Please refer to the appendix section 7.1 for further graphs.
![Image](./resources/C0362ADE016AE5705BCBDB218B5C8376.jpg =450x282)
![Image](./resources/59D97394956A0C72F877AC2DA57999F1.jpg =450x282)
We see that for different number of masses, there is a clear indication of a difference between the systems on whether does the pendulum return back to the initial state multiple times or not. We see that especially for a 10-mass sytem, the system returns back to its initial state numerous times. Furthermore, we note that the first return time for all the systems look like they occur approximately at the same time.























# Appendix
## 2. Varying the number of masses in the system
### 2.1 Position
![Image](./resources/9FF39E1E8A8801BE6B471A6425F43B50.jpg =1072x313)
![Image](./resources/E25ECD47B57BFD625384459AFF535762.jpg =1072x313)
![Image](./resources/A1A32F310DE53C76708D98046E02C0A1.jpg =1072x313)
![Image](./resources/817A637675CC4395CC4CDE93757EE6C2.jpg =1072x313)
![Image](./resources/608B4EC1A76B936A849D5DD9A8886A89.jpg =1072x313)
![Image](./resources/D1A837856F0B6E6A6D5C52E507BEB4D1.jpg =1072x313)
### 2.2 Velocity
![Image](./resources/88D2CA3F0607DF9104A4A22707714116.jpg =1072x313)
![Image](./resources/573989B21721A39FDBFA9F6D1ED46278.jpg =1072x313)
![Image](./resources/D39252C00A4DBE5B5A94EBB3F8B7FA50.jpg =1072x313)
![Image](./resources/1C8432DBD2699F5A00605FF9CC66A0A1.jpg =1072x313)
![Image](./resources/C2E9CFC852196764B15A9302A27F9C22.jpg =1072x313)
![Image](./resources/8F9E5377D00EDCDBA4D2A5C514317261.jpg =1072x313)

### 2.3 Energy
![Image](./resources/B97CE87F5865510BB87B6C83F8DB73AF.jpg =1072x568)
![Image](./resources/040A0ADB73EA2BB91633019153D4150C.jpg =1072x568)
![Image](./resources/CCF107C959DD70058A05927737FEE3CB.jpg =1072x568)

## 3. Varying initial conditions of the system
### 3.1 Position
**Note that the first pair of plots is from the chain's x and z position starting at the highest initial condition and the third pair of plot is of the chain's x and z position starting at the lowest initial condition.**
![Image](./resources/76C1A3C813830023A6208BD0F04AD595.jpg =1072x313)
![Image](./resources/F9DD652EE963576892201D708867D597.jpg =1072x313)
![Image](./resources/81D425BC7E4856267F09EAD570EFFECB.jpg =1072x313)
![Image](./resources/71126800223B0624EA0CBE0639A0999C.jpg =1072x313)
![Image](./resources/3326FF081F3B113598DEAFD930FBE7C6.jpg =1072x313)
![Image](./resources/524F09A251791B91EFB938DBE3BEBA7D.jpg =1072x313)
### 3.2 Velocity
**Note that the first pair of plots is from the chain's x and z velocity starting at the highest initial condition and the third pair of plot is of the chain's x and z velocity starting at the lowest initial condition.**
![Image](./resources/4EF12F0668DDE5718954A346A70BB200.jpg =1072x313)
![Image](./resources/827630C18F925758BF01D4178896A1C5.jpg =1072x313)
![Image](./resources/7805DA128EDAD145FC19845781D5227A.jpg =1072x313)
![Image](./resources/C96F0A1E30B61F95668FCA7022B5001E.jpg =1072x313)
![Image](./resources/141A4B9F79E4A7CC9EEBAA3CA032CC29.jpg =1072x313)
![Image](./resources/24886FD8B17D16A828EB98BA5DAF224E.jpg =1072x313)
### 3.3 Energy
**Note that the first plots is from the chain's energy starting at the highest initial condition and the third plot is of the chain's energy starting at the lowest initial condition.**
![Image](./resources/80322918B6BF1D85DAD44E03F448AACB.jpg =1072x568)
![Image](./resources/D01D7101B11BDCD952C6A14A64482112.jpg =1072x568)
![Image](./resources/06251F4FC4839E4B0B5BBDE36F927210.jpg =1072x568)

## 5. Distribution of angles
### 5.1 Graphs of distributions

![Image](./resources/08FE7E9F9C42A3E12A4AAF156ED19739.jpg =424x280)
![Image](./resources/CD5FAF1441E9FEEFB68FAC2E5C488948.jpg =424x280)
![Image](./resources/261CC0F730B6F8100B96C513AAC2882C.jpg =424x280)
![Image](./resources/32368ED6528107AB913AC36446A72D17.jpg =424x280)
![Image](./resources/96E065CB0B5D950CF87D3135CD28F2F1.jpg =424x280)
![Image](./resources/F569617106B2BF72368953F99CC23C66.jpg =424x280)
![Image](./resources/D1C8DA402422E7CFABAB218AD09A83E4.jpg =421x280)
![Image](./resources/2A4303D05235F6453843BB88D746AA0F.jpg =424x280)
![Image](./resources/CE97E98E65F705BADC9205CDEE23C81D.jpg =424x280)

## 7. Return Time
### 7.1 Return times for pendulums
![Image](./resources/C0362ADE016AE5705BCBDB218B5C8376.jpg =499x282)
![Image](./resources/16BF039291D3A9B8B895A87D6BF982D1.jpg =499x282)
![Image](./resources/D941D15C401BA7F0D67880F5B06A322B.jpg =499x282)
![Image](./resources/59D97394956A0C72F877AC2DA57999F1.jpg =499x282)