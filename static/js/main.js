import gsap from 'gsap'
import * as THREE from 'three';
import vertexShader from './shaders/vertex.glsl'
import fragmentShader from './shaders/fragment.glsl'
import './index.css'


import atmosphereVertexShader from './shaders/atmosphereVertex.glsl'
import atmosphereFragmentShader from './shaders/atmosphereFragment.glsl'
import { Float32BufferAttribute } from 'three';

const canvasContainer = document.querySelector('#canvasContainer')
const scene = new THREE.Scene();
const sizes = {
  width:window.innerWidth,
  height:window.innerHeight,
}
const camera = new THREE.
PerspectiveCamera(
  75,
  sizes.width/sizes.height,
  0.1,
  1000
)



const renderer = new THREE.WebGLRenderer(
  {
  antialias: true,
  canvas: document.querySelector('canvas')
  })

 
renderer.setSize(sizes.width,sizes.height)
renderer.setPixelRatio(window.devicePixelRatio)
 

//create a sphere
const sphere = new THREE.Mesh(
new THREE.SphereGeometry(5,50, 50) , 
new THREE.ShaderMaterial({
 
  vertexShader ,
  fragmentShader,
  uniforms:{
    globeTexture:{
      value:new THREE.TextureLoader().load('./img/MarsGlobe1.jpeg')
    }
  }
})
)

scene.add(sphere)


//create atmosphere
const atmosphere = new THREE.Mesh(
  new THREE.SphereGeometry(5,50, 50) , 
  new THREE.ShaderMaterial({
   
    vertexShader:atmosphereVertexShader ,
    fragmentShader:atmosphereFragmentShader,
    blending:THREE.AdditiveBlending,
    side:THREE.BackSide
  })
  )

  atmosphere.scale.set(1.1,1.1,1,1)
  scene.add(atmosphere)


  const group = new THREE.Group()
  group.add(sphere)
  scene.add(group)


  //adding stars
  const starGeometry = new THREE.BufferGeometry()
  const starMaterial = new THREE.PointsMaterial({
    color:0xffffff
  })

   const starVertices = []
   for(let i = 0; i < 10000; i++){
    const x = (Math.random()- 0.5)*2000
    const y = (Math.random()- 0.5)*2000
    const z = -(Math.random())*2000
    starVertices.push(x, y, z)
   }

   starGeometry.setAttribute('position',
   new THREE.Float32BufferAttribute(starVertices ,3))

  const stars = new THREE.Points(starGeometry, starMaterial)
  scene.add(stars)

camera.position.z = 15


const mouse = {
  x: undefined,
  y: undefined
}

function animate(){
  requestAnimationFrame(animate)
  renderer.render(scene, camera)
  sphere.rotation.y += 0.003
  group.rotation.y =  mouse.x * 0.5
  gsap.to(group.rotation,{
    x:-mouse.y*0.3,
    y: mouse.x * 0.5,
   duration:2
  })
}
animate()


addEventListener('mousemove',() =>{
  mouse.x = (event.clientX / innerWidth)* 2 - 1
  mouse.y = -(event.clientY / innerHeight)*2 - 1
})


//resizing
window.addEventListener('resize',()=>{
  //Update 
  sizes.width = window.innerWidth;
  sizes.height = window.innerHeight;
  //update camera
  
  camera.aspect = sizes.width/sizes.height;
  camera.updateProjectionMatrix()
  renderer.setSize(sizes.width/sizes.height)
})

const loop =()=>{
  rendrer.render(scene,camera);
  window.requestAnimationFrame(loop);
}

loop();

