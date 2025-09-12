<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:output method="html" encoding="UTF-8" indent="yes" />
  
  <xsl:template match="/">
    <html lang="es">
      <head>
        <meta charset="UTF-8" />
        <title>Tienda de Productos Singulares</title>
        <link rel="stylesheet" href="css/estilo.css" />
      </head>
      <body>
        <header>
          <h1>⭐ Tienda de Productos Singulares ⭐</h1>
        </header>
        
        <main>
          <section id="catalogo">
            <h2>🧪 Catálogo de Productos</h2>
            <div class="productos">
              <xsl:apply-templates select="//producto"/>
              <!-- Lista de productos-->
              <!-- <xsl:for-each select="//producto">
                <xsl:sort select="precio" order="descending"/>
                <div class="producto">
                  <img src="img/{imagen}" alt="{imagen}"/> 
                  <p><xsl:value-of select="nombre"/> 
                    <xsl:text> - Precio: </xsl:text>
                    <xsl:value-of select="precio"/><xsl:text> 💰 </xsl:text></p>
                </div>
              </xsl:for-each> -->
            </div>
          </section>
          <section id="destacados">
            <h2>✨ Productos destacados</h2>
            <div class="pr_destacados">
              <xsl:if test="count(//producto[@destacado='sí'])=0">
                <h2><xsl:text>No hay productos destacados</xsl:text></h2>
              </xsl:if>
                <xsl:for-each select="//producto[@destacado='sí']">
                  <div class="pr_destacado">
                    <img src="img/{imagen}" alt="{imagen}"/> 
                    <div class="pr_detalle">
                      <h3><xsl:value-of select="nombre"/></h3>
                    </div>
                  </div>
                </xsl:for-each>
            </div>
          </section>
          
          <section id="pedidos">
            <h2>🛒 Pedidos</h2>
            <div class="pedidos">
              <xsl:for-each select="//pedido">
                <xsl:variable name="cliente-id" select="@cliente"/>
                <xsl:variable name="cliente" select="//cliente[@id = $cliente-id]"/>
                <xsl:variable name="imagen-cliente" select="$cliente/imagen"/>
                <xsl:variable name="nombre-cliente" select="$cliente/nombre"/>
                <xsl:variable name="correo-cliente" select="$cliente/correo"/>
                
                <div class="pedido">
                  <div class="pd_detalle">
                    <img src="img/{$imagen-cliente}" alt="{$nombre-cliente}"/>
                    <div>
                      <h3>Pedido <xsl:value-of select="@id"/></h3>
                      <p><strong><xsl:value-of select="$nombre-cliente"/> / <xsl:value-of select="$correo-cliente"/></strong></p>
                      <p><strong>Fecha: </strong> <xsl:value-of select="@fecha"/></p>
                    </div>
                  </div>
                      <table>
                        <thead>
                          <tr>
                            <th>Producto</th>
                            <th>Cantidad</th>
                            <th>Total</th>
                          </tr>
                        </thead>
                        <tbody>
                          <xsl:for-each select="linea">
                            <xsl:variable name="producto-id" select="@producto"/>
                            <xsl:variable name="producto" select="/tienda/catalogo/producto[@id = $producto-id]"/>
                            <xsl:variable name="precio" select="number($producto/precio)"/>
                            <xsl:variable name="cantidad" select="number(@cantidad)"/>
                            <xsl:variable name="total" select="$cantidad * $precio"/>
                            
                            <tr>
                              <td><xsl:value-of select="$producto/nombre"/></td>
                              <td><xsl:value-of select="@cantidad"/></td>
                              <td><xsl:value-of select="format-number($total, '#.00')"/> 💰</td>
                            </tr>
                          </xsl:for-each>
                        </tbody>
                      </table>
                  </div>
              </xsl:for-each>
            </div>
          </section>
          <section id="catalogo">
            <h2>📦 Stock de productos</h2>
            <div class="productos">
                <!-- Lista de productos-->
                <xsl:for-each select="//producto">
                    <xsl:sort select="@unidades" data-type="number" order="ascending"/>
                    <div class="producto">
                      <img src="img/{imagen}" alt="{imagen}"/> 
                      <p><strong><xsl:value-of select="nombre"/></strong> - <xsl:value-of select="@unidades"/> unidades </p> 
                        <xsl:choose>
                          <xsl:when test="@unidades &gt; 10">
                            <p class="stock alto">✅ Stock alto</p>
                          </xsl:when>
                          <xsl:when test="@unidades &lt;= 10 and @unidades &gt; 5">
                            <p class="stock medio">⚠️ Stock medio</p>
                          </xsl:when>
                          <xsl:otherwise>
                            <p class="stock bajo"> 🛑 Quedan pocas unidades</p>
                          </xsl:otherwise>
                        </xsl:choose>
                    </div>
                  </xsl:for-each>
            </div>
          </section>
          <section id="estadisticas">
            <h2>📊 Estadísticas</h2>
            <div class="lista">
              <ol>
                <xsl:for-each select="//producto">
                  <xsl:sort 
                    select="number(precio)" 
                    data-type="number" 
                    order="ascending" />
                  <xsl:if test="position() = 1">
                    <li>
                      <h3>💸 Producto más barato:</h3>
                        <xsl:value-of select="nombre"/>
                        – 
                        <xsl:value-of select="precio"/> 💰
                    </li>
                  </xsl:if>
                  <xsl:if test="position() = last()">
                    <li>
                      <h3>💸💸 Producto más caro:</h3>
                        <xsl:value-of select="nombre"/>
                        – 
                        <xsl:value-of select="precio"/> 💰
                      </li>
                  </xsl:if>
                </xsl:for-each>
                <li>
                <xsl:for-each select="//producto">         
                  <xsl:sort 
                    select="sum(//linea[@producto = current()/@id]/@cantidad)" 
                    data-type="number" 
                    order="descending" />
                  <xsl:if test="position() = 1">
                    <h3>🏆 Producto más vendido:</h3>
                    <xsl:value-of select="nombre"/> 
                      (<xsl:value-of 
                        select="format-number(sum(//linea[@producto = current()/@id]/@cantidad), '#.##')"
                      /> unidades vendidas)
                  </xsl:if> 
                </xsl:for-each>
                </li>
                <li>
                  <xsl:variable name="total-unidades" select="sum(//linea/@cantidad)" />
                  <xsl:variable name="total-lineas" select="count(//linea)" />
                  <xsl:variable name="media" select="$total-unidades div $total-lineas" />

                  <h3>📊 Media de unidades por línea de pedido:</h3>
                  <xsl:value-of select="format-number($media, '#.00')"/> unidades
                </li>
              </ol>
            </div>
          </section>
        </main>
        <footer>
          <p>© 2025 Tienda de Pociones Mágicas</p>
        </footer>
        
      </body>
    </html>
  </xsl:template>
  
  <!-- Plantilla de tarjeta para cada producto -->
    <xsl:template match="producto">
       <div class="producto">
        <img src="img/{imagen}" alt="{imagen}"/>
        <p>
          <xsl:value-of select="nombre"/>
          <xsl:text> - Precio: </xsl:text>
          <xsl:value-of select="precio"/><xsl:text> 💰 </xsl:text>
        </p> 
       </div>
    </xsl:template>
       
 </xsl:stylesheet>
